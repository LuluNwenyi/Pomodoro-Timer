from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BROWN = "#251605"
PURPLE = "#ebd4fd"
FONT_NAME = "Montserrat"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(25*60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count /60)
    count_sec = count % 60

    if count < 10:
        count_sec =f"0{count_sec}"

    
   
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000, count_down, count-1)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodoro Timer")
#window.geometry("500x500")
window.config(padx=100, pady=50, bg=PURPLE)


title_label= Label(text="Timer", fg=BROWN, bg=PURPLE, font=(FONT_NAME, 45) )
title_label.grid(column=1, row=0)


canvas=Canvas(width=250, height=224, bg=PURPLE, highlightthickness=0)  #highlightthickness takes away the border around the canvas

tomato_img = PhotoImage(file="/Users/user/Desktop/GUI Practice/My_Pomodoro_Timer.py/tomato.png")
canvas.create_image(125, 112, image= tomato_img)
timer_text= canvas.create_text(125, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", bg= PURPLE, fg=BROWN, highlightthickness=2, highlightcolor=PURPLE, highlightbackground=PURPLE, command=start_timer)
reset_button = Button(text="Reset", bg= PURPLE, fg=BROWN, highlightthickness=2, highlightcolor=PURPLE, highlightbackground=PURPLE)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✅", bg=PURPLE)
check_marks.grid(column=1, row=3)

window.mainloop()