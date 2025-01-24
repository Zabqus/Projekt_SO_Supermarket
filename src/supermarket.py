
from multiprocessing import Process, Queue, Event
from queue import Empty
from .guard import SecurityGuard
import time
import random
import logging
from utils.config import Config


class CashierProcess(Process):



    def __init__(self, cashier_id, queue, fire_event):
        super().__init__()
        self.cashier_id = cashier_id
        self.queue = queue
        self.fire_event = fire_event
        self.is_active = True
        self.is_closing = False

    def run(self):
        logging.info(f"Kasjer {self.cashier_id + 1} zaczął pracę")
        while self.is_active and not self.fire_event.is_set():
            try:
                if self.is_closing and self.queue.empty():
                    logging.info(f"Kasjer {self.cashier_id + 1} zakończył pracę na kasie")
                    break

                customer = self.queue.get(timeout=1)
                if customer is not None and not self.fire_event.is_set():
                    self._serve_customer(customer)
            except Empty:
                continue
            except (KeyboardInterrupt, Exception) as e:
                logging.info(f"Kasjer  {self.cashier_id + 1} kończy pracę")
                break

    def _serve_customer(self, customer_id):
        service_time = random.uniform(5, 10) #czas na obsługę klienta przy kasie
        logging.info(f"Kasjer {self.cashier_id + 1} obsługiwał klienta {customer_id} przez {service_time:.2f}s")
        time.sleep(service_time)
        logging.info(f"Kasjer {self.cashier_id + 1} zakończył obsługiwanie klienta {customer_id}")


class Supermarket:
    def __init__(self, num_cashiers, min_active_cashiers):
        self.config = Config()
        self.num_cashiers = num_cashiers
        self.min_active_cashiers = min_active_cashiers

        self.fire_event = Event()
        self.queues = [Queue() for _ in range(num_cashiers)]
        self.cashiers = [None] * num_cashiers
        self.is_open = True
        self.total_customers = 0

        # Zaczynamy od kas 1 i 2
        self.active_cashier_numbers = [0, 1]

        logging.info(f" Przygotowanie {min_active_cashiers} kasjerów do otwarcia ")

        self.guard = SecurityGuard(self)
        self.guard.start()

    def start(self):
        logging.info("Otwarcie supermarketu")
        '''Uruchamiamy pierwsze dwie kasy'''
        self._start_cashier(0)
        self._start_cashier(1)

        while True:
            try:
                if self.is_open:
                    self._generate_customers()
                else:
                    time.sleep(1)
            except KeyboardInterrupt:
                logging.info("\n Otrzymanie sygnału zamknięcia sklepu")
                self.cleanup()
                break

    def _start_cashier(self, cashier_num):
        cashier = CashierProcess(cashier_num, self.queues[cashier_num], self.fire_event)
        cashier.start()
        self.cashiers[cashier_num] = cashier
        if cashier_num not in self.active_cashier_numbers:
            self.active_cashier_numbers.append(cashier_num)
        logging.info(f"Rozpoczęcie pracy kasjera nr {cashier_num + 1}")

    def _display_status(self):
        '''wyświetlanie statusu kas'''
        BLUE = '\033[94m'

        RESET = '\033[0m'

        logging.info(f"{BLUE}=== STATUS SUPERMARKETU ==={RESET}")
        logging.info(f"{BLUE}Active cashiers: {len(self.active_cashier_numbers)}{RESET}")
        for cashier_num in sorted(self.active_cashier_numbers):
            queue_size = self.queues[cashier_num].qsize()
            logging.info(f"{BLUE}Kasjer {cashier_num + 1}: {queue_size} klientów w kolejce{RESET}")
        logging.info(f"{BLUE}========================\n{RESET}")

    def _generate_customers(self):
        customer_id = 0
        last_status_time = time.time()

        while True:
            try:
                if not self.is_open or self.fire_event.is_set(): #sprawdzenie czy nie ma alarmu i czy sklep jest otwarty
                    time.sleep(1)
                    continue

                current_time = time.time()
                '''Czas co jaki ma się wyświetlić mam status sklepu'''
                if current_time - last_status_time >= 10:
                    self._display_status()
                    last_status_time = current_time

                customer_id += 1
                logging.info(f"Klient {customer_id} wszedł do sklepu")

                '''Symulacja chodzenia po sklepie'''
                shopping_time = random.uniform(0.5, 0.6)
                logging.info(f"Klient {customer_id} robił zakupy przez {shopping_time:.2f}s")
                time.sleep(shopping_time)
                '''Ponowne sprawdzenie po zakupach czy nie ma pożaru'''
                if self.is_open and not self.fire_event.is_set():
                    logging.info(f"klient {customer_id} zakończył robienie zakupów")
                    self._add_customer(customer_id)
                time.sleep(random.uniform(0.2, 0.5))

            except KeyboardInterrupt:
                break

    def _add_customer(self, customer_id):
        available_queues = []
        for cashier_num in self.active_cashier_numbers:
            if self.cashiers[cashier_num] and not self.cashiers[cashier_num].is_closing:
                available_queues.append((cashier_num, self.queues[cashier_num].qsize()))

        if available_queues:
            shortest_queue_idx = min(available_queues, key=lambda x: x[1])[0]
            self.queues[shortest_queue_idx].put(customer_id)
            self.total_customers += 1
            logging.info(f"Klient {customer_id} stanał w kolejce {shortest_queue_idx + 1}")
            self._update_cashiers()

    def _update_cashiers(self):
        total_customers = sum(self.queues[i].qsize() for i in self.active_cashier_numbers)
        current_active = len(self.active_cashier_numbers)

        if total_customers < self.config.CUSTOMERS_PER_CASHIER * (current_active - 1):
            if current_active > self.min_active_cashiers:
                self._close_random_cashier()
        else:
            required_cashiers = (total_customers // self.config.CUSTOMERS_PER_CASHIER) + 1
            if required_cashiers > current_active and current_active < self.num_cashiers:
                self._open_random_cashier()

    def _close_random_cashier(self):
        closeable_cashiers = [num for num in self.active_cashier_numbers if num > 1]
        if closeable_cashiers:
            to_close = random.choice(closeable_cashiers)
            logging.info(f"Kasjer {to_close + 1} zamknie kasę po obsłużeniu wszystkich klientów")
            self.cashiers[to_close].is_closing = True
            self.active_cashier_numbers.remove(to_close)

    def _open_random_cashier(self):
        available_numbers = set(range(self.num_cashiers)) - set(self.active_cashier_numbers)
        if available_numbers:
            new_cashier_num = random.choice(list(available_numbers))
            self._start_cashier(new_cashier_num)

    def cleanup(self):
        logging.info("\n Przygotowanie do zamknięcia sklepu ")
        self.is_open = False
        self.fire_event.set()

        '''Zatrzymanie strażaka'''
        if hasattr(self, 'guard') and self.guard is not None:
            try:
                self.guard.join(timeout=1.0)
            except Exception as e:
                logging.info(f"Zatrzymanie przez strażaka {e}")

        '''Zamykanie kas'''
        logging.info("Zamykanie wszystkich kas...")
        for cashier_num in sorted(self.active_cashier_numbers):
            if self.cashiers[cashier_num] is not None:
                print(f"Zamykanie kasjera {cashier_num + 1}")
                try:
                    self.cashiers[cashier_num].terminate()
                    self.cashiers[cashier_num].join(timeout=0.5)
                except Exception as e:
                    logging.info(f"Błąd przy zamykaniu kasy nr{cashier_num + 1}: {e}")

        '''Czyszczenie kolejek'''
        logging.info("Zamykanie kolejek ")
        for i, q in enumerate(self.queues):
            try:
                while not q.empty():
                    q.get_nowait()
            except Exception as e:
                logging.info(f"Błąd przy zamykaniu kolejki {i + 1}: {e}")

        print("Udane zamknięcie sklepu")
