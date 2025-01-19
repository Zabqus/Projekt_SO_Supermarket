import time
import random
from multiprocessing import Process, Queue, Event
from src.cashier import Cashier
from src.customer import Customer
from utils.config import Config
from src.guard import SecurityGuard
from queue import Empty

class CashierProcess(Process):


    def __init__(self, cashier_id, queue, fire_event):
        super().__init__()
        self.cashier_id = cashier_id
        self.queue = queue
        self.fire_event = fire_event
        self.is_active = True
        self.is_closing = False

    def run(self):
        print(f"Cashier {self.cashier_id + 1} started working")
        while self.is_active and not self.fire_event.is_set():
            try:
                if self.is_closing and self.queue.empty():
                    print(f"Cashier {self.cashier_id + 1} finished work and is now closed")
                    break

                customer = self.queue.get(timeout=1)
                if customer is not None:
                    self._serve_customer(customer)
            except Empty:
                continue
            except Exception as e:
                print(f"Cashier {self.cashier_id + 1} error: {e}")


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


        self.active_cashier_numbers = [0, 1]

        print(f" Przygotowanie {min_active_cashiers} kasjerów do otwarcia ")

        self.guard = SecurityGuard(self)
        self.guard.start()

    def start(self):
        print("Uruchamianie supermarketu")
        self._start_cashier(0)
        self._start_cashier(1)

        while True:
            try:
                if self.is_open:
                    self._generate_customers()
                else:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n Otrzymanie sygnału zamknięcia sklepu")
                self.cleanup()
                break

    def _generate_customers(self):
        customer_id = 0
        last_status_time = time.time()
        while self.is_open and not self.fire_event.is_set():
            try:

                current_time = time.time()
                if current_time - last_status_time >= 10:
                    self._display_status()
                    last_status_time = current_time

                customer_id += 1
                print(f"Klient {customer_id} wszedł do sklepu")
                shopping_time = random.uniform(0.5, 0.6) #czas na zakupy
                time.sleep(shopping_time)
                self._add_customer(customer_id)
                time.sleep(random.uniform(0.2, 0.5)) #co ile wchodzi klient

            except KeyboardInterrupt:
                raise

    def _add_customer(self, customer_id):
        available_queues = []
        for cashier_num in self.active_cashier_numbers:
            if self.cashiers[cashier_num]:
                available_queues.append((cashier_num, self.queues[cashier_num].qsize()))

        if available_queues:
            shortest_queue_idx = min(available_queues, key=lambda x: x[1])[0]
            self.queues[shortest_queue_idx].put(customer_id)
            self.total_customers += 1
            print(f"Klient {customer_id} dołączył do kolejki {shortest_queue_idx + 1}")

    def _start_cashier(self, cashier_num):
        cashier = CashierProcess(cashier_num, self.queues[cashier_num], self.fire_event)
        cashier.start()
        self.cashiers[cashier_num] = cashier
        if cashier_num not in self.active_cashier_numbers:
            self.active_cashier_numbers.append(cashier_num)
        print(f"Rozpoczęcie pracy kasjera nr {cashier_num + 1}")

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

    def _close_random_cashier(self): #zamknięcie gdy K*(N-1)
        closeable_cashiers = [num for num in self.active_cashier_numbers if num > 1]
        if closeable_cashiers:
            to_close = random.choice(closeable_cashiers)
            print(f"Kasa {to_close + 1} zostanie zamknięta")
            self.active_cashier_numbers.remove(to_close)


    def _open_random_cashier(self): #otwacie losowej kasy
        available_numbers = set(range(self.num_cashiers)) - set(self.active_cashier_numbers)
        if available_numbers:
            new_cashier_num = random.choice(list(available_numbers))
            self._start_cashier(new_cashier_num)

    def _display_status(self):
        print("\nSTATUS")
        print(f"Aktywne kasy: {len(self.active_cashier_numbers)}")
        for cashier_num in sorted(self.active_cashier_numbers):
            queue_size = self.queues[cashier_num].qsize()
            print(f"Kasa {cashier_num + 1}ma {queue_size} klientów w kolejce")
            print(f"\n")

    def cleanup(self):
        print("\n Przygotowanie do zamknięcia sklepu ")
        self.is_open = False
        self.fire_event.set()

        #stop na strażaka
        if hasattr(self, 'guard') and self.guard is not None:
            try:
                self.guard.join(timeout=1.0)
            except Exception as e:
                print(f"Zatrzymanie przez strażaka {e}")


        print("Zamykanie wszystkich kas...")
        for cashier_num in sorted(self.active_cashier_numbers):
            if self.cashiers[cashier_num] is not None:
                print(f"Zamykanie kasjera {cashier_num + 1}")
                try:
                    self.cashiers[cashier_num].terminate()
                    self.cashiers[cashier_num].join(timeout=0.5)
                except Exception as e:
                    print(f"Błąd przy zamykaniu kasy nr{cashier_num + 1}: {e}")

        print("Zamykanie kolejek ")
        for i, q in enumerate(self.queues):
            try:
                while not q.empty():
                    q.get_nowait()
            except Exception as e:
                print(f"Błąd przy zamykaniu kolejki {i + 1}: {e}")

        print("Udane zamknięcie sklepu")