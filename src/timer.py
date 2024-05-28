
import threading
from time import perf_counter, sleep


class Timer:
    def __init__(self, time: int = 10) -> None:
        self.time = time
        self.time_left = time
    
    def _completed(self) -> None:
        print("Timer finished!")
        self.time_left = self.time
    
    def _update_timer(self) -> None:
        current_time = perf_counter()
        self.time_left -= current_time - self._start_time
        self._start_time = current_time
        
    def start(self) -> None:
        self._start_time = perf_counter()
        self._delay_timer = threading.Timer(self.time_left, self._completed)
        self._delay_timer.start()

    def stop(self) -> None:
        self._delay_timer.cancel()
        self._update_timer()
    
    def get_time_left(self) -> None:
        self._update_timer()
        return self.time_left