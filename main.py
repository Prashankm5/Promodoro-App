from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Currier"
WORK_MIN = .5
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = .10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    win.after_cancel(timer)
    tittle_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        tittle_label.config(text='Long', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        tittle_label.config(text='Short', fg=PINK)
    else:
        count_down(work_sec)
        tittle_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f'0{count_min}'
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")

    if count > 0:
        global timer
        timer = win.after(1000, count_down, count-1)

    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"

        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title('Pomodoro')
win.config(padx=100, pady=50, background=YELLOW)



canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

tittle_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
tittle_label.grid(row=0, column=1)




reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, "normal"))
check_label.grid(row=3, column=1)

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)



win.mainloop()


