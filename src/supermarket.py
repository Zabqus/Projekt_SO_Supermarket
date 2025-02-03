import os
import time
import random
import logging
import signal
from utils.config import Config
from utils.shared_memory_queue import SharedMemoryQueue, Empty
from utils.signal_system import SignalSystem
from .guard import SecurityGuard
from .customer import Customer


class Supermarket:
    def __init__(self, num_cashiers, min_active_cashiers):
        self.config = Config()
        self.num_cashiers = num_cashiers
        self.min_active_cashiers = min_active_cashiers

        # System sygnałów
        self.signal_system = SignalSystem()

        self.shared_queue = SharedMemoryQueue()
        self.cashiers = [None] * num_cashiers
        self.is_open = True
        self.total_customers = 0
        self.customers = []  # lista wątków klientów

        # Rozpoczynamy z minimum 2 kasjerami
        self.active_cashier_numbers = [0, 1]

        logging.info(f"Przygotowanie {min_active_cashiers} kasjerów do otwarcia")

        self.guard = SecurityGuard(self)
        self.guard.start()

    def start(self):
        logging.info("Otwarcie supermarketu")
        self._start_cashier(0)
        self._start_cashier(1)

        try:
            while True:
                if self.is_open and not self.signal_system.is_fire():
                    self._generate_customers()
                time.sleep(0.1)
        except KeyboardInterrupt:
            logging.info("\nOtrzymanie sygnału zamknięcia sklepu")
            self.cleanup()

    def _start_cashier(self, cashier_num):
        pid = os.fork()

        if pid == 0:
            from .cashier import start_cashier
            start_cashier(cashier_num, self.shared_queue)
        else:
            self.cashiers[cashier_num] = pid
            self.signal_system.register_child(pid)
            if cashier_num not in self.active_cashier_numbers:
                self.active_cashier_numbers.append(cashier_num)

    def _display_status(self):
        BLUE = '\033[94m'
        RESET = '\033[0m'

        queue_size = self.shared_queue.qsize()
        active_cashiers = len(self.active_cashier_numbers)

        logging.info(f"{BLUE}=== STATUS SUPERMARKETU ==={RESET}")
        logging.info(f"{BLUE}Aktywne kasy: {active_cashiers}{RESET}")
        logging.info(f"{BLUE}Liczba klientów w kolejce: {queue_size}{RESET}")
        logging.info(f"{BLUE}========================\n{RESET}")

    def _generate_customers(self):
        """Generowanie i obsługa klientów"""
        try:
            if not self.is_open or self.signal_system.is_fire():
                return

            # status na sklepie
            current_time = time.time()
            if not hasattr(self, 'last_status_time'):
                self.last_status_time = current_time
            elif current_time - self.last_status_time >= 10:
                self._display_status()
                self.last_status_time = current_time

            # nowy klient = wątek
            customer_id = self.total_customers + 1
            new_customer = Customer(customer_id, self)
            self.customers.append(new_customer)
            new_customer.start()
            self.total_customers += 1

            # Opóźnienie przed następnym klientem
            time.sleep(random.uniform(0.5, 1))

        except Exception as e:
            logging.error(f"Błąd podczas generowania klienta: {e}")

    '''def _add_customer(self, customer_id):
        if len(self.active_cashier_numbers) > 0:
            self.shared_queue.put(customer_id)
            self.total_customers += 1
            logging.info(f"Klient {customer_id} stanął w kolejce")
            self._update_cashiers()'''

    def _update_cashiers(self):
        queue_size = self.shared_queue.qsize()
        current_active = len(self.active_cashier_numbers)


        required_cashiers = max(
            self.config.MIN_ACTIVE_CASHIERS,
            queue_size // self.config.CUSTOMERS_PER_CASHIER + 1
        )


        if current_active < required_cashiers and current_active < self.config.NUM_CASHIERS:
            available = list(set(range(self.config.NUM_CASHIERS)) - set(self.active_cashier_numbers))
            if available:
                self._start_cashier(available[0])


        elif queue_size < self.config.CUSTOMERS_PER_CASHIER * (current_active - 1):
            if current_active > self.config.MIN_ACTIVE_CASHIERS:
                self._close_random_cashier()

    def _close_random_cashier(self):
        closeable_cashiers = [num for num in self.active_cashier_numbers if num > 1]
        if closeable_cashiers:
            to_close = random.choice(closeable_cashiers)
            logging.info(f"Kasjer {to_close + 1} zostanie zamknięty po obsłużeniu kolejki")
            os.kill(self.cashiers[to_close], signal.SIGTERM)
            self.active_cashier_numbers.remove(to_close)

    def _open_random_cashier(self):
        available_numbers = set(range(self.num_cashiers)) - set(self.active_cashier_numbers)
        if available_numbers:
            new_cashier_num = random.choice(list(available_numbers))
            self._start_cashier(new_cashier_num)

    def cleanup(self):
        if hasattr(self, '_cleanup_started') and self._cleanup_started:
            return

        self._cleanup_started = True
        self.is_open = False

        # Zatrzymanie wątków klientów
        for customer in self.customers:
            customer.is_shopping = False
            try:
                customer.join(timeout=1.0)
            except:
                pass

        # Zamykanie procesów kasjerów
        for cashier_num in sorted(self.active_cashier_numbers):
            try:
                if self.cashiers[cashier_num]:
                    os.kill(self.cashiers[cashier_num], signal.SIGTERM)
                    pid, _ = os.waitpid(self.cashiers[cashier_num], os.WNOHANG)
                    if pid == 0:
                        time.sleep(0.5)
                        os.waitpid(self.cashiers[cashier_num], 0)
            except:
                pass

        # Czyszczenie pozostałych procesów potomnych
        try:
            while True:
                pid, _ = os.waitpid(-1, os.WNOHANG)
                if pid <= 0:
                    break
        except ChildProcessError:
            pass

        # Czyszczenie zasobów
        try:
            self.shared_queue.close()
            if hasattr(self, 'guard'):
                self.guard.stop()
        except:
            pass

        print("Supermarket zamknięty")