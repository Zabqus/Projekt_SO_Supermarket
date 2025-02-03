import os
import time
import random
import signal
import logging
from utils.shared_memory_queue import SharedMemoryQueue, Empty


class Cashier:
    def __init__(self, cashier_id, shared_queue):
        self.cashier_id = cashier_id
        self.shared_queue = shared_queue
        self.is_active = True

    def run(self):
        """Główna pętla procesu kasjera"""
        signal.signal(signal.SIGTERM, self._handle_terminate)
        signal.signal(signal.SIGUSR1, self._handle_fire)

        logging.info(f"Kasjer {self.cashier_id + 1} rozpoczyna pracę")

        while self.is_active:
            try:

                customer = self.shared_queue.get(timeout=0.2)
                if customer is not None and self.is_active:
                    self._serve_customer(customer)
            except Empty:

                continue
            except Exception as e:
                logging.error(f"Błąd kasjera {self.cashier_id + 1}: {e}")
                break

        logging.info(f"Kasjer {self.cashier_id + 1} kończy pracę")

    def _serve_customer(self, customer_id):
        """Obsługa pojedynczego klienta"""
        service_time = random.uniform(2, 4)
        logging.info(f"Kasjer {self.cashier_id + 1} obsługuje klienta {customer_id} przez {service_time:.2f}s")
        time.sleep(service_time)
        logging.info(f"Kasjer {self.cashier_id + 1} zakończył obsługę klienta {customer_id}")

    def _handle_terminate(self, signum, frame):
        """Obsługa sygnału zakończenia pracy"""
        logging.info(f"Kasjer {self.cashier_id + 1} otrzymał sygnał zakończenia pracy")
        self.is_active = False

    def _handle_fire(self, signum, frame):
        """Obsługa sygnału pożaru"""
        logging.info(f"Kasjer {self.cashier_id + 1} otrzymał sygnał pożaru")
        self.is_active = False


def start_cashier(cashier_id, shared_queue):
    """Funkcja startowa dla procesu kasjera"""
    try:
        cashier = Cashier(cashier_id, shared_queue)
        cashier.run()
    except Exception as e:
        logging.error(f"Krytyczny błąd kasjera {cashier_id + 1}: {e}")
    finally:
        os._exit(0)