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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text,text = "00:00")
    label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label1.config(text= "WORK", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        reps = 0
        label1.config(text="BREAK", fg=RED)
    elif reps %2 == 0:
        count_down(short_break_sec)
        label1.config(text="BREAK",fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    min = math.floor(count/60)
    sec = (count % 60)
    if sec<10 :
        sec = f"0{sec}"

    #if len(str(sec) ) ==1:
    #    sec = "0"+ str(sec)

    canvas.itemconfig(timer_text, text= f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_mark = ""
        for i in range(math.floor(reps/2)):
            check_mark += "✔"
        label2.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg= YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)



label1 = Label(text= "Timer", bg=YELLOW ,fg =GREEN, font=(FONT_NAME,50,"bold"))
label1.grid(row=0,column=1)

label2 = Label(bg=YELLOW, fg=GREEN)
label2.grid(row=3,column=1)

button1 = Button(text="Start",  highlightthickness=0, command= start_timer)
button1.grid(row=2, column=0)

button2= Button(text="Reset", highlightthickness=0,command= reset_timer)
button2.grid(row=2,column=2)





window.mainloop()