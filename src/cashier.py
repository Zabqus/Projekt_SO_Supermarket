from multiprocessing import Process
import time
import random
import logging

class Cashier(Process):
   def __init__(self, id, customer_sem, customer_queue, fire_event):
       super().__init__()
       self.id = id
       self.is_active = True
       self.customer_sem = customer_sem
       self.customer_queue = customer_queue
       self.fire_event = fire_event
       '''Losowy czas obsługi klienta przez kasjera'''
       self.service_time = random.uniform(3, 5)

   def run(self):
       while self.is_active and not self.fire_event.is_set():
           try:
               if self.fire_event.is_set():
                   break
               with self.customer_sem:
                   '''Próba pobrania klienta z kolejki z timeoutem'''
                   customer = self.customer_queue.get(timeout=0.2)
                   if not self.fire_event.is_set():
                       self._serve_customer(customer)
           except:
               continue

   '''Symulacja obsługi klienta'''
   def _serve_customer(self, customer):
       time.sleep(self.service_time)
       customer.service_complete.set()