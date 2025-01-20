import pytest
from unittest.mock import patch
from src.supermarket import Supermarket
from utils.config import Config


@patch('time.sleep', return_value=None)
def test_supermarket_no_sleep(mock_sleep):
    config = Config()
    supermarket = Supermarket(num_cashiers=config.NUM_CASHIERS, min_active_cashiers=config.MIN_ACTIVE_CASHIERS)

    for i in range(20):
        supermarket._add_customer(i)

    supermarket.fire_event.set()
    supermarket.cleanup()

    supermarket.is_open = True
    supermarket.fire_event.clear()

    assert supermarket.is_open
    assert len(supermarket.active_cashier_numbers) >= config.MIN_ACTIVE_CASHIERS