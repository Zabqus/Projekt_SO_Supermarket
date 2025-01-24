from threading import Thread
from multiprocessing import Queue, Event
import time
import random
import signal
import logging

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

class SecurityGuard(Thread):
    def __init__(self, supermarket):
        super().__init__()
        self.supermarket = supermarket
        self.daemon = True

    def run(self):
        while True:
            if not self.supermarket.fire_event.is_set():
                '''Losowy czas do następnego alarmu'''
                alarm_time = random.uniform(60, 180)
                time.sleep(alarm_time)
                self.trigger_fire_alarm()

    def trigger_fire_alarm(self):
        logging.info(f"\n{RED}!!! UWAGA ALARM POŻAROWY !!!")
        logging.info(f" EWAKUACJA WSZYSTKICH W SUPERMARKECIE {RESET}")


        self.supermarket.is_open = False
        self.supermarket.fire_event.set()
        '''status na pożar'''
        time.sleep(2.5)
        '''czas na zamknięcie procesów'''
        self.stop_all_cashiers()
        self.evacuate_customers()
        self.close_cashiers()

        logging.info(f"\n{RED} Ewakuacja klientów i zamkniecie kas")
        logging.info(f"Czekanie aż pożar zostanie ugaszony {RESET}")
        time.sleep(15)

        self.reopen_supermarket()

    def stop_all_cashiers(self):
        for cashier in self.supermarket.cashiers:
            if cashier is not None:
                cashier.terminate()
                cashier.join(timeout=0.1)
        self.supermarket.cashiers = [None] * self.supermarket.num_cashiers

    def evacuate_customers(self):
        logging.info(f"{RED}Ewakuowanie klientów")
        for queue in self.supermarket.queues:
            while not queue.empty():
                try:
                    customer = queue.get_nowait()
                    logging.info(f"Klient {customer} został ewakuowany ze sklepu")
                except:
                    continue
        self.supermarket.total_customers = 0
        logging.info(f"{RESET}")

    def close_cashiers(self):
        logging.info(f"{RED}zamykanie wszystkich kas do ewakuacji")
        for cashier in self.supermarket.cashiers:
            if cashier is not None:
                cashier.is_closing = True
                time.sleep(0.1)
                cashier.terminate()
                cashier.join(timeout=0.5)
        self.supermarket.cashiers = [None] * self.supermarket.num_cashiers

    def reopen_supermarket(self):
        logging.info(f"\n{GREEN} Ponowne otwrcie supermarketu")
        self.supermarket.fire_event.clear()
        self.supermarket.is_open = True
        self.supermarket.total_customers = 0

        self.supermarket.cashiers = [None] * self.supermarket.num_cashiers
        self.supermarket.active_cashier_numbers = [0, 1]
        '''rozpoczęcie sklepu z 2 kasjerami'''
        self.supermarket.queues = [Queue() for _ in range(self.supermarket.num_cashiers)]


        self.supermarket._start_cashier(0)
        self.supermarket._start_cashier(1)
        logging.info(f"Skep otwarty i gotowy do przyjścia klientów{RESET}")