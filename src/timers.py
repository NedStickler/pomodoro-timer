
import threading
import winsound
from time import perf_counter, sleep


class Timer:
    def __init__(self, time: int = 60) -> None:
        self.time = time
        self.time_left = time
        self.ticking = False
        self.completed = False
    
    def _completed(self) -> None:
        self.completed = True
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
        self.completed = False
        self.ticking = True
        self._start_time = perf_counter()
        self._delay_timer = threading.Timer(self.time_left, self._completed)
        self._delay_timer.start()

    def stop(self) -> None:
        if self.ticking:
            self._delay_timer.cancel()
            self._update_timer()
            self.ticking = False
    
    def reset(self) -> None:
        if self.ticking:
            self._delay_timer.cancel()
        self.completed = False
        self.time_left = self.time
        self.ticking = False
    
    def get_time_left(self) -> None:
        self._update_timer()
        return self.time_left
    
    def set_time(self, time: int) -> None:
        if not self.ticking:
            self.time = time
            self.time_left = time
    

class PomodoroTimer(Timer):
    def __init__(self, work, brk) -> None:
        super().__init__(work)
        self.work = work
        self.brk = brk
        self.current = "work"
    
    def _completed(self) -> None:
        self.completed = True
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
    
    def reset(self) -> None:
        self.completed = False

        if self.ticking:
            self.ticking = False
            self._delay_timer.cancel()

        if self.current == "work":
            self.time_left = self.work
        else:
            self.time_left = self.brk
    
    def set_work(self, time: int) -> None:
        if not self.ticking:
            self.work = time
            if self.current == "work":
                self.time_left = time
        self._update_timer()

    def set_break(self, time: int) -> None:
        if not self.ticking:
            self.brk = time
            if self.current == "break":
                self.time_left = time
        self._update_timer()
        