from multiprocessing import Queue
from threading import Lock



class QueueManager:
    def __init__(self, max_queues):
        self.max_queues = max_queues
        self.queues = {}
        self.lock = Lock()
        self.customer_count = 0

    def create_queue(self, cashier_id):
        with self.lock:
            if len(self.queues) < self.max_queues:
                self.queues[cashier_id] = Queue()
                return True
            return False

    def remove_queue(self, cashier_id):
        with self.lock:
            if cashier_id in self.queues:
                del self.queues[cashier_id]
                return True
            return False

    def add_customer(self, cashier_id, customer):
        if cashier_id in self.queues:
            self.queues[cashier_id].put(customer)
            with self.lock:
                self.customer_count += 1
            return True
        return False

    def get_next_customer(self, cashier_id):
        if cashier_id in self.queues and not self.queues[cashier_id].empty():
            customer = self.queues[cashier_id].get()
            with self.lock:
                self.customer_count -= 1
            return customer
        return None

    def get_shortest_queue(self):
        min_length = float('inf')
        best_queue = None

        for cashier_id, queue in self.queues.items():
            length = queue.qsize()
            if length < min_length:
                min_length = length
                best_queue = cashier_id

        return best_queue

    def empty_all_queues(self):
        with self.lock:
            for queue in self.queues.values():
                while not queue.empty():
                    try:
                        queue.get_nowait()
                    except:
                        continue
            self.customer_count = 0