# timer.py

import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self, duration=25*60):
        self._start_time = None
        self.duration = duration 

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def get_elapsed_time(self):
        """Return the elapsed time"""
        return time.perf_counter() - self._start_time

    def timer_is_up(self):
        """Check the elapsed time, and return True
           if the timer is up"""
        return self.get_elapsed_time() >= self.duration
