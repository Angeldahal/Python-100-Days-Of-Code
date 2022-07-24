import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20 
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text= "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_marks.config(text = "")
     

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN  * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%2 != 0 and reps < 8 :
        title_label.config(text = "Work",fg= RED)
        count_down(work_sec)
        reps += 1
    elif reps < 7:
        title_label.config(text = "Break",fg = GREEN)
        count_down(short_break_sec)
        reps += 1
    elif reps == 8:
        title_label.config(text = "Break",fg = GREEN)
        count_down(long_break_sec)
        reps = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✅"
        check_marks.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


canvas = Canvas(width = 200, height= 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image = tomato_image)
timer_text = canvas.create_text(103, 130, text = "00:00", fill = "white",font =(FONT_NAME, 35,"bold"))
canvas.grid(column = 1, row = 1)


title_label = Label(text = "Timer")
title_label.config(font = (FONT_NAME,40, "bold"), fg = GREEN, bg = YELLOW)
title_label.grid(column = 1, row = 0)

start_button = Button(text = "Start",command = start_timer, highlightthickness=0)
start_button.grid(column = 0, row = 3)

reset_button = Button(text = "Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column = 3, row = 3)

check_marks = Label( bg = YELLOW)
check_marks.grid(column = 1, row = 3)












window.mainloop()