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
                alarm_time = random.uniform(150, 250) # czas co ile jest alarm
                time.sleep(alarm_time)
                self.trigger_fire_alarm()



    def trigger_fire_alarm(self):
        print("\n!!! ALARM POŻAROWY !!!")
        print("ROZPOCZĘTO EWAKUACJĘ")
        self.supermarket.is_open = False