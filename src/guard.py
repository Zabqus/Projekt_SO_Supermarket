from threading import Thread
import time
import random

class SecurityGuard(Thread):
    def __init__(self, supermarket):
        super().__init__()
        self.supermarket = supermarket
        self.daemon = True



    def run(self):
        while True:
            if not self.supermarket.fire_event.is_set():
                alarm_time = random.uniform(15, 20) # czas co ile jest alarm
                time.sleep(alarm_time)
                self.trigger_fire_alarm()



    def trigger_fire_alarm(self):
        print("\n!!! ALARM POŻAROWY !!!")
        print("ROZPOCZĘTO EWAKUACJĘ")
        self.supermarket.is_open = False
        self.supermarket.fire_event.set()
        self.evacuate_customers()
        self.close_cashiers()

    def evacuate_customers(self):
        print("Ewakuacja")
        for queue in self.supermarket.queues:
            while not queue.empty():
                try:
                    customer = queue.get_nowait()
                    print(f"Klient {customer} ewakuowany")
                except:
                    continue
        self.supermarket.total_customers = 0

    def close_cashiers(self):
        print(f"zamykanie wszystkich kas do ewakuacji")
        # Zamknięcie wszystkich kas
        for cashier in self.supermarket.cashiers:
            if cashier is not None:
                cashier.terminate()
                cashier.join(timeout=0.5)
        self.supermarket.cashiers = [None] * self.supermarket.num_cashiers
