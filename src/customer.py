from threading import Thread, Event
import time
import random

class Customer(Thread):
    def __init__(self, id, supermarket):
        super().__init__()
        self.id = id
        self.supermarket = supermarket
        self.is_shopping = True
        self.service_complete = Event()
    def run(self):
        self._do_shopping()
        if self.is_shopping:
            self._queue_for_checkout()
    def _do_shopping(self):
        time.sleep(random.uniform(1, 5))

    def _queue_for_checkout(self):
        self.supermarket.customer_queue.put(self)
        self.service_complete.set()

#evacuation?