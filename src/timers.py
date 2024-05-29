
import threading
import winsound
from time import perf_counter, sleep


class Timer:
    def __init__(self, time: int = 60) -> None:
        self.time = time
        self.time_left = time
        self.ticking = False
    
    def _completed(self) -> None:
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
        self.ticking = False
    
    def get_time_left(self) -> None:
        self._update_timer()
        return self.time_left
    
    def set_time(self, time: int) -> None:
        self.time = time
        if not self.ticking:
            self.time_left = time
    

class PomodoroTimer(Timer):
    def __init__(self, work, brk) -> None:
        super().__init__(work)
        self.work = work
        self.brk = brk
        self.current = "work"
    
    def _completed(self) -> None:
        self.ticking = False
        if self.current == "work":
            self.time_left = self.brk
            self.current = "break"
            for _ in range(5):
                winsound.Beep(880, 300)
        else:
            self.time_left = self.work
            self.current = "work"
            for _ in range(3):
                winsound.Beep(440, 500)
    
