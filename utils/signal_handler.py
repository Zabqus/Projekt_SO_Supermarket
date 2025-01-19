import signal
import sys
import time

class SignalHandler:
    def __init__(self):
        self.received_signal = False
        self.fire_alarm = False

    def handle_shutdown(self, signum, frame):
        self.received_signal = True
        print("\nZamykanie supermarketu...")
        sys.exit(0)

    def handle_fire(self, signum, frame):
        self.fire_alarm = True
        print("\nALARM POŻAROWY! Ewakuacja supermarketu...")