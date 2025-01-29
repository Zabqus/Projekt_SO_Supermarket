class Config:
    def __init__(self):
        self.NUM_CASHIERS = 10          # całkowita liczba kas
        self.MIN_ACTIVE_CASHIERS = 2    # min liczba aktywnych kas
        self.CUSTOMERS_PER_CASHIER = 5  # liczba K z zadania - ilu klientów na jedną kasę
        self.MAX_QUEUE_SIZE = 50        # max rozmiar kolejki
        self.SHARED_MEMORY_SIZE = (2 + self.NUM_CASHIERS) * 4 #pamięc współdzielona
