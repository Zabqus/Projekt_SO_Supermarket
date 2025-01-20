import pytest
from src.supermarket import Supermarket
from utils.config import Config


def test_cashier_scaling():
    config = Config()
    supermarket = Supermarket(num_cashiers=config.NUM_CASHIERS, min_active_cashiers=config.MIN_ACTIVE_CASHIERS)

    customers_needed = config.CUSTOMERS_PER_CASHIER * 3
    for i in range(customers_needed):
        supermarket._add_customer(i)
    assert len(supermarket.active_cashier_numbers) > config.MIN_ACTIVE_CASHIERS

    for queue in supermarket.queues:
        while not queue.empty():
            queue.get()
    supermarket._update_cashiers()
    assert len(supermarket.active_cashier_numbers) == config.MIN_ACTIVE_CASHIERS