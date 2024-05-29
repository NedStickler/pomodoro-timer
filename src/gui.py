
import datetime
from tkinter import *
from timers import PomodoroTimer

def update_label():
    time.config(text=str(datetime.timedelta(seconds=int(timer.get_time_left()))))
    root.after(1, update_label)

if __name__ == "__main__":
    root = Tk()
    timer = PomodoroTimer(10, 3)

    time = Label(root, text=str(datetime.timedelta(seconds=int(timer.get_time_left()))))
    start = Button(root, text="Start", command=timer.start)
    stop = Button(root, text="Stop", command=timer.stop)
    reset = Button(root, text="Reset", command=timer.reset)

    time.pack()
    start.pack()
    stop.pack()
    reset.pack()

    update_label()

    root.mainloop()