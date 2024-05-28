
import threading
from time import perf_counter

# TODO:
# - perf_counter before threading.Timer
# - Set off threading.Timer
# - If paused before (using cancel) then take difference of perf_counter before and after, subtract from time_left
# - When timer completes, reset time left to length

class Timer:
    def __init__(self, length: int) -> None:
        self.length = length
        self.time_left = length

    def start(self):
        print("Timer finished!")
        self.time_left = self.length
    
    def get_time(self):
        return self.time_left