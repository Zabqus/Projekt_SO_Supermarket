import time
import random
from multiprocessing import Process, Queue
from .cashier import Cashier
from .customer import Customer
from utils.config import Config


class Supermarket:
    def __init__(self, num_cashiers, min_active_cashiers):
        self.config = Config()
        self.num_cashiers = num_cashiers
        self.min_active_cashiers = min_active_cashiers

        self.queues = [Queue() for _ in range(num_cashiers)]
        self.cashiers = [None] * num_cashiers
        self.is_open = True
        self.total_customers = 0

        self.active_cashier_numbers = [0, 1]

    def start(self):
        self._start_cashier(0)
        self._start_cashier(1)

    def _start_cashier(self, cashier_num):
        cashier = Cashier(cashier_num, self.queues[cashier_num])
        cashier.start()
        self.cashiers[cashier_num] = cashier