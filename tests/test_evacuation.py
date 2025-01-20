import pytest
from src.supermarket import Supermarket
from utils.config import Config


def test_emergency_evacuation():
    config = Config()
    supermarket = Supermarket(num_cashiers=config.NUM_CASHIERS, min_active_cashiers=config.MIN_ACTIVE_CASHIERS)

    for i in range(5):
        supermarket._add_customer(i)

    initial_customers = supermarket.total_customers
    assert initial_customers > 0  #

    supermarket.fire_event.set()
    supermarket.cleanup()

    assert supermarket.total_customers == 0
    assert all(q.empty() for q in supermarket.queues)
    assert not supermarket.is_open