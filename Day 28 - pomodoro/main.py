from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(my_timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark['text'] = ''


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
        
    if reps % 8 == 0:
        countdown(long_break_time)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_time)
        label.config(text="Break", fg=PINK)
    else:
        countdown(work_time)
        label.config(text="Work", fg=GREEN)
            

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark['text']+="✔"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)



start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(font=(FONT_NAME, 15, "bold"),bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)

window.mainloop()