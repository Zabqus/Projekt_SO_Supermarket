import signal


class SignalHandler:
    def __init__(self):
        self.should_terminate = False

    def handle_shutdown(self, signum, frame):
        print("\nOtrzymano sygnał zamknięcia")
        self.should_terminate = True