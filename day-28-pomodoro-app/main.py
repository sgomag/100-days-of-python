from tkinter import *
import tkinter.messagebox
import math
import sys
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#f26849"
GREEN = "#379b46"
LIGHT_GREEN = "#c2dcb3"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
pomodoros = ""
timer = None
count = None

# ---------------------------- BACKGROUND & WINDOW CHANGE ------------------------------- #
def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)
    except AttributeError:
        return relative_path

def background_color(color):
    canvas.config(bg=color)
    window.config(bg=color)
    checkmark.config(bg=color)
    test.config(bg=color)
    header.config(bg=color)
    button_reset.config(bg=color, activebackground=color)
    button_start.config(bg=color, activebackground=color)

def bring_to_front():
    # Restore if window is minimized
    window.state("normal")
    # Bring to top level above all windows
    window.attributes("-topmost", True)
    # Allows other windows to top level again
    window.attributes("-topmost", False)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    header.config(text="Pomodoro", fg=GREEN)
    button_start.config(text="Start")
    global reps
    reps = 0
    global marks
    marks = ""
    checkmark.config(text=marks)
    background_color(YELLOW)
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_or_pause():
    global count
    global timer
    global reps
    if reps == 0: #Start
        sec = next_session()
        count_down(sec)
        button_start.config(text="Pause")
    elif timer is not None: #Pause
        window.after_cancel(timer)
        timer = None
        button_start.config(text="Resume")
    else: #Resume
        timer = window.after(100, count_down, count - 1)
        button_start.config(text="Pause")

def next_session():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message=f"Ready for a {LONG_BREAK_MIN} min. break?")
        background_color(LIGHT_GREEN)
        header.config(fg=GREEN, text="Long break")
        return long_break_sec

    elif reps % 2 == 0:
        tkinter.messagebox.showinfo(title="Break", message=f"Ready for a {SHORT_BREAK_MIN} min. break?")
        background_color(LIGHT_GREEN)
        header.config(fg=GREEN, text="Break")
        return short_break_sec

    else:
        if reps != 1:
            tkinter.messagebox.showinfo(title="Work", message=f"Ready to work for {WORK_MIN} min.?")
        background_color(YELLOW)
        header.config(fg=RED, text="Work")
        return work_sec


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(sec):
    global count
    global reps
    global marks
    global pomodoros
    count_min = math.floor(sec / 60)
    count_sec = sec % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    count = sec
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        bring_to_front()
        sec = next_session()
        count_down(sec)
        if reps % 8 == 1:
            marks = ""
            checkmark.config(text=marks)
            pomodoros += "🔴"
            test.config(text=f"{pomodoros}")
        elif reps % 2 == 0:
            marks += "✔"
            checkmark.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

canvas = Canvas(width=200 , height=224, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
window.iconphoto(False, tomato_img)
canvas.grid(column=1, row=1)


header = Label(text="Pomodoro", font=(FONT_NAME, 24, "bold"), pady=6, fg=GREEN)
header.grid(column=1, row=0)

button_start = Button(text = "Start", command=start_or_pause)
button_start.config(relief="groove", width=7, pady=6, font=(FONT_NAME, 10, "normal"))
button_start.grid(column=0, row=2)

button_reset = Button(text = "Reset", command=reset_timer)
button_reset.config(relief="groove", width=7, pady=6, font=(FONT_NAME, 10, "normal"))
button_reset.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 10, "bold"), pady=20, fg=GREEN)
checkmark.grid(column=1, row=2)

test = Label(font=(FONT_NAME, 10, "bold"), pady=00, fg=RED)
test.grid(column=1, row=3)

background_color(YELLOW)

window.mainloop()