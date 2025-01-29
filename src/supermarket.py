import os
import time
import random
import logging
import signal
from utils.config import Config
from utils.shared_memory_queue import SharedMemoryQueue, Empty
from utils.signal_system import SignalSystem
from .guard import SecurityGuard


class Supermarket:
    def __init__(self, num_cashiers, min_active_cashiers):
        self.config = Config()
        self.num_cashiers = num_cashiers
        self.min_active_cashiers = min_active_cashiers

        # System sygnałów
        self.signal_system = SignalSystem()

        # Jedna współdzielona kolejka
        self.shared_queue = SharedMemoryQueue()
        self.cashiers = [None] * num_cashiers
        self.is_open = True
        self.total_customers = 0

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
            while True:  # Zmiana warunku pętli
                if self.is_open and not self.signal_system.is_fire():
                    self._generate_customers()
                time.sleep(0.1)
        except KeyboardInterrupt:
            logging.info("\nOtrzymanie sygnału zamknięcia sklepu")
            self.cleanup()

    def _start_cashier(self, cashier_num):
        pid = os.fork()

        if pid == 0:  # Proces potomny (kasjer)
            from .cashier import start_cashier
            start_cashier(cashier_num, self.shared_queue)
        else:  # Proces rodzica
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

            # Sprawdzenie i aktualizacja statusu
            current_time = time.time()
            if not hasattr(self, 'last_status_time'):
                self.last_status_time = current_time
            elif current_time - self.last_status_time >= 10:
                self._display_status()
                self.last_status_time = current_time

            # Generowanie nowego klienta
            customer_id = self.total_customers + 1
            logging.info(f"Klient {customer_id} wszedł do sklepu")

            # Symulacja zakupów
            shopping_time = random.uniform(0.5, 1)
            logging.info(f"Klient {customer_id} robi zakupy przez {shopping_time:.2f}s")
            time.sleep(shopping_time)

            # Dodanie klienta do kolejki jeśli sklep nadal otwarty
            if self.is_open and not self.signal_system.is_fire():
                logging.info(f"Klient {customer_id} zakończył zakupy")
                self._add_customer(customer_id)

            # Opóźnienie przed następnym klientem
            time.sleep(random.uniform(0.2, 0.3))

        except Exception as e:
            logging.error(f"Błąd podczas generowania klienta: {e}")

    def _add_customer(self, customer_id):
        if len(self.active_cashier_numbers) > 0:
            self.shared_queue.put(customer_id)
            self.total_customers += 1
            logging.info(f"Klient {customer_id} stanął w kolejce")
            self._update_cashiers()

    def _update_cashiers(self):
        queue_size = self.shared_queue.qsize()
        current_active = len(self.active_cashier_numbers)

        if queue_size < self.config.CUSTOMERS_PER_CASHIER * (current_active - 1):
            if current_active > self.min_active_cashiers:
                self._close_random_cashier()
        else:
            required_cashiers = (queue_size // self.config.CUSTOMERS_PER_CASHIER) + 1
            if required_cashiers > current_active and current_active < self.num_cashiers:
                self._open_random_cashier()

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

        # Zamykanie kasjerów
        for cashier_num in sorted(self.active_cashier_numbers):
            try:
                if self.cashiers[cashier_num]:
                    os.kill(self.cashiers[cashier_num], signal.SIGTERM)
                    os.waitpid(self.cashiers[cashier_num], 0)
            except:
                pass

        #czyszczenie kolejki
        try:
            self.shared_queue.close()
            if hasattr(self, 'guard'):
                self.guard.stop()
        except:
            pass

        print("Supermarket zamknięty")