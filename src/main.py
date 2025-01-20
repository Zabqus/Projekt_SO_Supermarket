import signal
import sys
import os
from src.supermarket import Supermarket
from utils.config import Config
from utils.signal_handler import SignalHandler
import logging
from utils.logging_config import setup_logging


def main():
    '''start logowania do pliku '''
    log_filename = setup_logging()
    logging.info("Otwarcie supermarketu")
    logging.info(f"PID procesu głównego: {os.getpid()}")

    '''Inicjalizacja obsługi sygnałów'''
    signal_handler = SignalHandler()

    '''Sygnały dla wydarzeń'''
    signal.signal(signal.SIGINT, signal_handler.handle_shutdown)
    signal.signal(signal.SIGTERM, signal_handler.handle_shutdown)
    signal.signal(signal.SIGUSR1, signal_handler.handle_fire)

    config = Config()

    try:
        supermarket = Supermarket(
            num_cashiers=config.NUM_CASHIERS,
            min_active_cashiers=config.MIN_ACTIVE_CASHIERS
        )
        supermarket.start()

        signal.pause()

    except Exception as e:
        logging.error(f"Błąd: {e}")
        sys.exit(1)
    finally:
        if 'supermarket' in locals():
            logging.info("Zamykanie supermarketu...")
            supermarket.cleanup()
            logging.info("Supermarket zamknięty")


if __name__ == "__main__":
    main()