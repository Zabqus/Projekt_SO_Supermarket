from threading import Thread
import time
import random
import signal
import logging
import os
import sys

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'


class SecurityGuard(Thread):
    def __init__(self, supermarket):
        super().__init__()
        self.supermarket = supermarket
        self.daemon = True
        self.active = True
        signal.signal(signal.SIGUSR1, self._handle_alarm)

    def _handle_alarm(self, signum, frame):
        if signum == signal.SIGUSR1:
            self.trigger_fire_alarm()

    def run(self):
        while self.active:
            if not self.supermarket.signal_system.is_fire():
                alarm_time = random.uniform(30,45 )
                time.sleep(alarm_time)
                if self.active:
                    self.trigger_fire_alarm()

    def trigger_fire_alarm(self):
        if not self.supermarket.signal_system.is_fire():
            logging.info(f"\n{RED}!!! UWAGA ALARM POŻAROWY !!!")
            logging.info(f" EWAKUACJA WSZYSTKICH W SUPERMARKECIE {RESET}")

            self.supermarket.signal_system.set_fire()
            self.supermarket.is_open = False

            self.stop_all_cashiers()  # Najpierw zatrzymaj kasjerów
            self.evacuate_customers()  # Potem ewakuuj klientów

            logging.info(f"{RED}Sklep został zamknięty z powodu alarmu pożarowego{RESET}")
            os.kill(os.getppid(), signal.SIGINT)

    def stop_all_cashiers(self):
        # Wysłanie SIGTERM
        for pid in self.supermarket.cashiers:
            if pid is not None:
                try:
                    os.kill(pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass

        time.sleep(1)

        self.supermarket.cashiers = [None] * self.supermarket.num_cashiers

    def evacuate_customers(self):
        logging.info(f"{RED}Ewakuowanie klientów")
        try:
            while not self.supermarket.shared_queue.empty():
                customer = self.supermarket.shared_queue.get()
                logging.info(f"Klient {customer} został ewakuowany ze sklepu")
        except Exception as e:
            logging.error(f" {e}")

        self.supermarket.total_customers = 0


    def stop(self):
        self.active = False