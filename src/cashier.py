from multiprocessing import Process
import time
import random

class Cashier(Process):
    def __init__(self, id, customer_queue):
        super().__init__()
        self.id = id
        self.is_active = True
        self.customer_queue = customer_queue
        self.service_time = random.uniform(3, 5)

    def run(self):
        while self.is_active:
            try:
                customer = self.customer_queue.get(timeout=1)
                if customer is not None:
                    self._serve_customer(customer)
            except:
                continue

    def _serve_customer(self, customer):
        time.sleep(self.service_time)
        print(f"kasa {self.id + 1} zakończyła obsługę klienta {customer}")