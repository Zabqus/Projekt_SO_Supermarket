import pytest
from src.supermarket import Supermarket
from utils.config import Config


def test_min_cashiers_rule():
    config = Config()
    supermarket = Supermarket(num_cashiers=config.NUM_CASHIERS, min_active_cashiers=config.MIN_ACTIVE_CASHIERS)

    supermarket.active_cashiers = 1
    supermarket._update_cashiers()
    assert len(supermarket.active_cashier_numbers) >= config.MIN_ACTIVE_CASHIERS

    for _ in range(3):
        supermarket._update_cashiers()
        assert len(supermarket.active_cashier_numbers) >= 2