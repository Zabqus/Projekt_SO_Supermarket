import sys
from src.supermarket import Supermarket
from utils.config import Config


def main():
    config = Config()

    try:
        supermarket = Supermarket(
            num_cashiers=config.NUM_CASHIERS,
            min_active_cashiers=config.MIN_ACTIVE_CASHIERS
        )
        supermarket.start()

    except KeyboardInterrupt:
        print("\nOtrzymano sygnał zakończenia")
    except Exception as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'supermarket' in locals():
            supermarket.cleanup()


if __name__ == "__main__":
    main()