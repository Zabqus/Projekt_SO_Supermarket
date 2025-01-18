import time
import random
from multiprocessing import Process, Queue
from src.cashier import Cashier
from src.customer import Customer
from utils.config import Config


class Supermarket:
    def __init__(self, num_cashiers, min_active_cashiers):
        self.config = Config()
        self.num_cashiers = num_cashiers
        self.min_active_cashiers = min_active_cashiers

        self.queues = [Queue() for _ in range(num_cashiers)]
        self.cashiers = [None] * num_cashiers
        self.is_open = True
        self.total_customers = 0

        self.active_cashier_numbers = [0, 1]

    def start(self):
        print("Uruchamianie supermarketu")
        self._start_cashier(0)
        self._start_cashier(1)

        try:
            self._generate_customers()
        except KeyboardInterrupt:
            print("\nOtrzymano sygnał zakończenia")
            self.cleanup()

    def _generate_customers(self):
        customer_id = 0

        while self.is_open:
            try:
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
        cashier = Cashier(cashier_num, self.queues[cashier_num])
        cashier.start()
        self.cashiers[cashier_num] = cashier

    def _update_cashiers(self):  #zarządzanie kasami
        total_customers = sum(self.queues[i].qsize() for i in self.active_cashier_numbers)
        current_active = len(self.active_cashier_numbers)

        if current_active < self.num_cashiers and total_customers > current_active * 5:
            self._open_random_cashier()
        elif current_active > self.min_active_cashiers and total_customers < (current_active - 1) * 5:
            self._close_random_cashier()

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

    def cleanup(self):
        print("\nZamykanie supermarketu...")
        self.is_open = False

        for cashier in self.cashiers:
            if cashier is not None:
                cashier.terminate()
                cashier.join()

        for q in self.queues:
            while not q.empty():
                try:
                    q.get_nowait()
                except:
                    continue

        print("Supermarket zamknięty")