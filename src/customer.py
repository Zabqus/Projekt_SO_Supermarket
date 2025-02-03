import os
import time
import random
import logging
import signal
from threading import Thread


class Customer(Thread):
    def __init__(self, id, supermarket):
        super().__init__()
        self.id = id
        self.supermarket = supermarket
        self.is_shopping = True
        self._setup_signal_handlers()

    def _setup_signal_handlers(self):
        """Ustawienie obsługi sygnałów dla klienta"""
        signal.signal(signal.SIGUSR1, self._handle_evacuation)

    def _handle_evacuation(self, signum, frame):
        """Obsługa sygnału ewakuacji"""
        self.is_shopping = False
        logging.info(f"Klient {self.id} przerywa zakupy i ewakuuje się")

    def run(self):
        try:
            if not self.supermarket.signal_system.is_fire():
                self._do_shopping()
                if self.is_shopping:
                    self._queue_for_checkout()
        except Exception as e:
            logging.error(f"Błąd podczas obsługi klienta {self.id}: {e}")

    def _do_shopping(self):
        """Symulacja robienia zakupów"""
        try:
            shopping_time = random.uniform(1, 5)
            logging.info(f"Klient {self.id} robi zakupy przez {shopping_time:.2f}s")

            '''interwały tak aby była lepsza reakcja na ewakuację'''
            intervals = int(shopping_time / 0.5)
            for _ in range(intervals):
                if not self.is_shopping or self.supermarket.signal_system.is_fire():
                    logging.info(f"Klient {self.id} przerywa zakupy")
                    return
                time.sleep(0.5)

            if shopping_time % 0.5 > 0:
                time.sleep(shopping_time % 0.5)

        except Exception as e:
            logging.error(f"Błąd podczas zakupów klienta {self.id}: {e}")
            self.is_shopping = False

    def _queue_for_checkout(self):
        """Dołączenie do kolejki do kasy"""
        try:
            if not self.is_shopping or self.supermarket.signal_system.is_fire():
                return

            logging.info(f"Klient {self.id} staje w kolejce")
            self.supermarket.shared_queue.put(self.id)
            self.supermarket._update_cashiers()  # Dodaj to wywołanie

            while self.is_shopping and not self.supermarket.signal_system.is_fire():
                time.sleep(0.1)

        except Exception as e:
            logging.error(f"Błąd podczas ustawiania się w kolejce klienta {self.id}: {e}")

    def evacuate(self):
        """Wywołanie ewakuacji klienta"""
        self.is_shopping = False
        os.kill(os.getpid(), signal.SIGUSR1)