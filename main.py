from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BROWN = "#251605"
PURPLE = "#ebd4fd"
FONT_NAME = "Montserrat"
VIOLET = "#7b2cbf"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer) #to stop it
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text= "Timer", fg= BROWN)
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec= WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #for 8th rep
    if reps % 8 ==0:
         count_down(long_break_sec)
         title_label.config(text="Break", fg= RED)

     #for 2nd,4th,6th rep
    elif reps % 2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg= PINK)
    
    #for 1st, 3rd, 5th or 7th rep
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg= VIOLET)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    

   
    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps/2) #no of work sessions
        for _ in range(work_sessions):
            mark += "✅"
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro Timer")
#window.geometry("500x500")
window.config(padx=50, pady=50, bg=PURPLE)
window.resizable(0,0)

title_label= Label(text="Timer", fg=BROWN, bg=PURPLE, font=(FONT_NAME, 45) )
title_label.grid(column=1, row=0)


canvas=Canvas(width=250, height=224, bg=PURPLE, highlightthickness=0)  #highlightthickness takes away the border around the canvas

tomato_img = PhotoImage(file="/Users/user/Desktop/GUI Practice/My_Pomodoro_Timer.py/tomato.png")
canvas.create_image(125, 112, image= tomato_img)
timer_text= canvas.create_text(125, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", bg= PURPLE, fg=BROWN, highlightthickness=2, highlightcolor=PURPLE, highlightbackground=PURPLE, command=start_timer)
reset_button = Button(text="Reset", bg= PURPLE, fg=BROWN, highlightthickness=2, highlightcolor=PURPLE, highlightbackground=PURPLE, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = Label(text=" ", bg=PURPLE)
check_marks.grid(column=1, row=3)

window.mainloop()