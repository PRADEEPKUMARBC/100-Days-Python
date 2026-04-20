from tkinter import *
import math

# ---------------- CONSTANTS ---------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdecc"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks = 0

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    # Timer_text "00:00"


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 1st/3rd/5th/7th
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 35))

    # if it's the 8th rep:
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))

    # if it's 2nd/4th/6th rep:
    else:
        count_down(work_sec)

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec == "0":
        count_sec = "00"
    if count_sec <= 10:
        count_sec = "0" + str(count_sec)
    if count_min == "0":
        count_min = "00"
    if count_min <= 10:
        count_min = "0" + str(count_min)


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

window = Tk()
window.title("My first GUI")
window.config(padx=100, pady=50, bg=PINK)

# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000, say_something, 3, 5, 8)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00",  fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

count_down(5)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()