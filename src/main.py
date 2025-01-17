import signal
import sys
from multiprocessing import freeze_support
from src.supermarket import Supermarket
from utils.config import Config
from utils.signal_handler import SignalHandler

def main():
    signal_handler = SignalHandler()
    signal.signal(signal.SIGINT, signal_handler.handle_shutdown)
    signal.signal(signal.SIGTERM, signal_handler.handle_shutdown)

    config = Config()

    try:
        supermarket = Supermarket(
            num_cashiers=config.NUM_CASHIERS,
            min_active_cashiers=config.MIN_ACTIVE_CASHIERS
        )
        supermarket.start()



    except Exception as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'supermarket' in locals():
            supermarket.cleanup()

if __name__ == "__main__":
    freeze_support()
    main()