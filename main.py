import signal
import sys
import os
from src.supermarket import Supermarket
from utils.config import Config
from utils.logging_config import setup_logging
import logging

def setup_signal_handlers(supermarket):
    def handle_shutdown(signum, frame):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        if not hasattr(supermarket, '_cleanup_started'):
            print("\nZamykanie supermarketu...")
            supermarket.cleanup()
        sys.exit(0)

    def handle_fire(signum, frame):
        if not supermarket.signal_system.is_fire():
            print("\nALARM POŻAROWY")
            supermarket.signal_system.set_fire()

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGUSR1, handle_fire)

def main():
    log_filename = setup_logging()
    logging.info("Otwarcie supermarketu")
    logging.info(f"PID procesu głównego: {os.getpid()}")

    config = Config()

    try:
        supermarket = Supermarket(
            num_cashiers=config.NUM_CASHIERS,
            min_active_cashiers=config.MIN_ACTIVE_CASHIERS
        )
        setup_signal_handlers(supermarket)
        supermarket.start()

    except Exception as e:
        logging.error(f"Błąd krytyczny: {e}")
        sys.exit(1)
    finally:
        if 'supermarket' in locals() and not supermarket.signal_system.is_fire():
            logging.info("Zamykanie supermarketu...")
            supermarket.cleanup()
            logging.info("Supermarket zamknięty")

if __name__ == "__main__":
    main()