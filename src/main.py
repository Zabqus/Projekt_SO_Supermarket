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
        if 'supermarket' in locals():
            supermarket.cleanup()


if __name__ == "__main__":
    main()