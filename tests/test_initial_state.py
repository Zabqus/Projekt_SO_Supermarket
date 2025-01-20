import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.supermarket import Supermarket
from utils.config import Config

def test_initial_state():
    config = Config()
    supermarket = Supermarket(num_cashiers=config.NUM_CASHIERS, min_active_cashiers=config.MIN_ACTIVE_CASHIERS)

    assert len(supermarket.active_cashier_numbers) == config.MIN_ACTIVE_CASHIERS
    assert supermarket.is_open == True
    assert supermarket.total_customers == 0
    assert len(supermarket.cashiers) == config.NUM_CASHIERS

    assert 0 in supermarket.active_cashier_numbers
    assert 1 in supermarket.active_cashier_numbers