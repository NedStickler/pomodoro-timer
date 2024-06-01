
import datetime
from tkinter import *
from timers import PomodoroTimer


def update_category():
    if timer.current == "work":
        timer_colour = "#5DADE2"
    else:
        timer_colour = "#28B463"
    category.config(text=timer.current.title(), bg=timer_colour, fg="white")
    root.after(1, update_category)

def update_time():
    if timer.current == "work":
        timer_colour = "#5DADE2"
    else:
        timer_colour = "#28B463"
    time.config(text=str(datetime.timedelta(seconds=int(timer.get_time_left()))), bg=timer_colour, fg="white")
    root.after(1, update_time)

def continue_timer():
    if timer.completed:
        timer.start()
    root.after(1, continue_timer)

def set_work_time():
    if (h := hours.get()) == "":
        h = 0
    if (m := minutes.get()) == "":
        m = 0
    if (s := seconds.get()) == "":
        s = 0
    try:
        time = int(h)*60**2 + int(m)*60 + int(s)
        timer.set_work(time)
    except ValueError:
        return

def set_break_time():
    if (h := hours.get()) == "":
        h = 0
    if (m := minutes.get()) == "":
        m = 0
    if (s := seconds.get()) == "":
        s = 0
        
    try:
        time = int(h)*60**2 + int(m)*60 + int(s)
        timer.set_break(time)
    except ValueError:
        return

if __name__ == "__main__":
    # Root window setup
    root = Tk()
    root.geometry("240x210")
    root.title("Pomodoro Timer")
    root.resizable(False, False)
    root.configure(bg="#273746")
    
    # Setup frames to act as parent widgets
    timer_buttons_frame = Frame(root)
    input_boxes_frame = Frame(root)
    set_time_frame = Frame(root)

    timer = PomodoroTimer(1500, 300)
    timer_colour = "#5DADE2"

    # Work/break label and timer
    category = Label(root, text=timer.current.title(), font=("Century Gothic", 18), bg=timer_colour, fg="white")
    time = Label(root, text=str(datetime.timedelta(seconds=int(timer.get_time_left()))), font=("Century Gothic", 46), bg=timer_colour, fg="white")

    # Timer buttons
    start = Button(timer_buttons_frame, text="Start", command=timer.start, relief="flat", bg="#273746", fg="white", font=("Century Gothic", 16))
    stop = Button(timer_buttons_frame, text="Stop", command=timer.stop, relief="flat", bg="#273746", fg="white", font=("Century Gothic", 16))
    reset = Button(timer_buttons_frame, text="Reset", command=timer.reset, relief="flat", bg="#273746", fg="white", font=("Century Gothic", 16))
    start.place(width=80, height=40)
    stop.place(width=80, height=40, x=80, y=0)
    reset.place(width=80, height=40, x=160, y=0)

    # Input boxes
    hours = Entry(input_boxes_frame, bg="#2C3E50", relief="flat", fg="white", font=("Century Gothic", 22), justify="center", insertbackground="white")
    minutes = Entry(input_boxes_frame, bg="#2C3E50", relief="flat", fg="white", font=("Century Gothic", 22), justify="center", insertbackground="white")
    seconds = Entry(input_boxes_frame, bg="#2C3E50", relief="flat", fg="white", font=("Century Gothic", 22), justify="center", insertbackground="white")
    hours.insert(0, "0")
    minutes.insert(0, "25")
    seconds.insert(0, "0")
    hours_label = Label(input_boxes_frame, text="h", bg="#2C3E50", fg="white", font=("Century Gothic", 14))
    minutes_label = Label(input_boxes_frame, text="m", bg="#2C3E50", fg="white", font=("Century Gothic", 14))
    seconds_label = Label(input_boxes_frame, text="s", bg="#2C3E50", fg="white", font=("Century Gothic", 14))
    hours.place(width=60, height=40, x=0, y=0)
    hours_label.place(width=20, height=40, x=60, y=0)
    minutes.place(width=60, height=40, x=80, y=0)
    minutes_label.place(width=20, height=40, x=140, y=0)
    seconds.place(width=60, height=40, x=160, y=0)
    seconds_label.place(width=20, height=40, x=220, y=0)

    # Set timer lengths buttons
    set_work = Button(set_time_frame, text="Set work", command=set_work_time, relief="flat", bg="#273746", fg="white", font=("Century Gothic", 11))
    set_break = Button(set_time_frame, text="Set break", command=set_break_time, relief="flat", bg="#273746", fg="white", font=("Century Gothic", 11))
    set_work.place(width=120, height=20, x=0, y=0)
    set_break.place(width=120, height=20, x=120, y=0)

    # Place frames
    category.place(x=0, y=0, width=240, height=30)
    time.place(x=0, y=30, width=240, height=80)
    timer_buttons_frame.place(x=0, y=110, width=240, height=40)
    input_boxes_frame.place(x=0, y=150, width=240, height=40)
    set_time_frame.place(x=0, y=190, width=240, height=20)
    
    update_category()
    update_time()
    continue_timer()
    category.update()
    time.update()

    root.mainloop()