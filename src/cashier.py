from multiprocessing import Process
import time
import random




class Cashier(Process):
    def __init__(self, id, customer_sem, customer_queue):
        super().__init__()
        self.id = id
        self.is_active = True
        self.customer_sem = customer_sem
        self.customer_queue = customer_queue
        self.service_time = random.uniform(3, 5) #czas na obsługe klientów




    def run(self):
        while self.is_active:
            try:
                with self.customer_sem:
                    customer = self.customer_queue.get(timeout=1)
                    self._serve_customer(customer)
            except:
                continue

    def _serve_customer(self, customer):
        time.sleep(self.service_time)


#evacuation