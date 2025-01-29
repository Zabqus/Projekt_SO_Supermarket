import os
import signal
import logging


class SignalSystem:
    def __init__(self):
        self._fire_signal = False
        self._child_pids = set()

        # Ustawienie obsługi sygnałów
        signal.signal(signal.SIGUSR1, self._handle_fire)
        signal.signal(signal.SIGCHLD, self._handle_child)

    def _handle_fire(self, signum, frame):
        if not self._fire_signal:  # Dodajemy zabezpieczenie
            self._fire_signal = True
            # Przekazanie sygnału tylko do procesów potomnych
            for pid in self._child_pids:
                try:
                    os.kill(pid, signal.SIGUSR1)
                except ProcessLookupError:
                    self._child_pids.discard(pid)

    def _handle_child(self, signum, frame):
        """Obsługa zakończenia procesu potomnego"""
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid:
                self._child_pids.discard(pid)
        except ChildProcessError:
            pass

    def register_child(self, pid):
        """Rejestracja nowego procesu potomnego"""
        self._child_pids.add(pid)

    def is_fire(self):
        """Sprawdzenie czy jest pożar"""
        return self._fire_signal

    def set_fire(self):
        """Ustawienie sygnału pożaru"""
        if not self._fire_signal:  # Dodajemy zabezpieczenie
            self._fire_signal = True
            # Przekazujemy sygnał tylko do procesów potomnych
            for pid in self._child_pids:
                try:
                    os.kill(pid, signal.SIGUSR1)
                except ProcessLookupError:
                    self._child_pids.discard(pid)

    def clear_fire(self):
        """Wyczyszczenie sygnału pożaru"""
        self._fire_signal = False
        for pid in self._child_pids:
            try:
                os.kill(pid, signal.SIGUSR2)
            except ProcessLookupError:
                self._child_pids.discard(pid)

    def cleanup(self):
        """Zakończenie wszystkich procesów potomnych"""
        for pid in self._child_pids.copy():
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                self._child_pids.discard(pid)