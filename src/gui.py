
import datetime
from tkinter import *
from timers import PomodoroTimer


def update_category():
    category.config(text=timer.current.title())
    root.after(1, update_category)

def update_time():
    time.config(text=str(datetime.timedelta(seconds=int(timer.get_time_left()))))
    root.after(1, update_time)

def continue_timer():
    if timer.completed:
        timer.start()
    root.after(1, continue_timer)

def set_work_time():
    time = int(hours.get())*60**2 + int(minutes.get())*60 + int(seconds.get())
    timer.set_work(time)

def set_break_time():
    time = int(hours.get())*60**2 + int(minutes.get())*60 + int(seconds.get())
    timer.set_break(time)

if __name__ == "__main__":
    # Root window setup
    root = Tk()
    root.geometry("240x220")
    root.title("Pomodoro Timer")
    root.resizable(False, False)

    # Setup frames to act as parent widgets
    timer_buttons_frame = Frame(root)
    input_boxes_frame = Frame(root)
    set_time_frame = Frame(root)

    timer = PomodoroTimer(1500, 300)

    # Work/break label and timer
    category = Label(root, text=timer.current.title(), font=("Arial", 18))
    time = Label(root, text=str(datetime.timedelta(seconds=int(timer.get_time_left()))), font=("Arial", 50))

    # Timer buttons
    start = Button(timer_buttons_frame, text="Start", command=timer.start)
    stop = Button(timer_buttons_frame, text="Stop", command=timer.stop)
    reset = Button(timer_buttons_frame, text="Reset", command=timer.reset)
    start.place(width=80, height=40)
    stop.place(width=80, height=40, x=80, y=0)
    reset.place(width=80, height=40, x=160, y=0)

    # Input boxes
    hours = Spinbox(input_boxes_frame, from_=0, to=100, increment=1, justify="center")
    minutes = Spinbox(input_boxes_frame, from_=0, to=59, increment=1, justify="center")
    seconds = Spinbox(input_boxes_frame, from_=1, to=59, increment=1, justify="center")
    hours_label = Label(input_boxes_frame, text="h")
    minutes_label = Label(input_boxes_frame, text="m")
    seconds_label = Label(input_boxes_frame, text="s")
    hours.place(width=60, height=20, x=0, y=0)
    hours_label.place(width=20, height=20, x=60, y=0)
    minutes.place(width=60, height=20, x=80, y=0)
    minutes_label.place(width=20, height=20, x=140, y=0)
    seconds.place(width=60, height=20, x=160, y=0)
    seconds_label.place(width=20, height=20, x=220, y=0)

    # Set timer lengths buttons
    set_work = Button(set_time_frame, text="Set work time", command=set_work_time)
    set_break = Button(set_time_frame, text="Set break time", command=set_break_time)
    set_work.place(width=120, height=20, x=0, y=0)
    set_break.place(width=120, height=20, x=120, y=0)

    category.place(x=0, y=0, width=240, height=40)
    time.place(x=0, y=40, width=240, height=80)
    timer_buttons_frame.place(x=0, y=120, width=240, height=40)
    input_boxes_frame.place(x=0, y=180, width=240, height=20)
    set_time_frame.place(x=0, y=200, width=240, height=20)
    
    update_category()
    update_time()
    continue_timer()

    root.mainloop()