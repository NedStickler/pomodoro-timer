
from time import perf_counter

class Timer:
    def __init__(self, length: int) -> None:
        self.length = length
        self.time_left = length
        self.ticking = False

    def start(self):
        self.ticking = True
        start_tick = perf_counter()
        while self.ticking and self.time_left > 0:
            self.time_left = self.length - (perf_counter() - start_tick)
            print(self.time_left)
        if self.time_left <= 0:
            print("Timer finished!")

    def stop(self):
        self.ticking = False
    
    def get_time(self):
        return self.time_left