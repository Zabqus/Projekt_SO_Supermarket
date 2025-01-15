from threading import Thread
import time
import random

class Customer(Thread):
    def __init__(self, id, supermarket):
        super().__init__()
        self.id = id
        self.supermarket = supermarket
        self.is_shopping = True

    def run(self):
        self._do_shopping()

    def _do_shopping(self):
        time.sleep(random.uniform(1, 5))

#registers
#queue
#evacuation?