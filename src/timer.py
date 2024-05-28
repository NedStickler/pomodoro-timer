
import threading
import winsound
from time import perf_counter, sleep


class Timer:
    def __init__(self, time: int = 10) -> None:
        self.time = time
        self.time_left = time
        self.ticking = False
    
    def _completed(self) -> True:
        self.time_left = self.time
        self.ticking = False
        for _ in range(5):
            winsound.Beep(880, 300)
    
    def _update_timer(self) -> None:
        if self.ticking:
            current_time = perf_counter()
            self.time_left -= current_time - self._start_time
            self._start_time = current_time
        
    def start(self) -> None:
        self.ticking = True
        self._start_time = perf_counter()
        self._delay_timer = threading.Timer(self.time_left, self._completed)
        self._delay_timer.start()

    def stop(self) -> None:
        self._delay_timer.cancel()
        self._update_timer()
        self.ticking = False
    
    def reset(self) -> None:
        if self.ticking:
            self._delay_timer.cancel()
        self.time_left = self.time
        ticking = False
    
    def get_time_left(self) -> None:
        self._update_timer()
        return self.time_left