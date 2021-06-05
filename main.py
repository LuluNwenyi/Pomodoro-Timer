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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodoro Timer")
#window.geometry("500x500")

canvas=Canvas(width=250, height=224)

tomato_img = PhotoImage(file="/Users/user/Desktop/GUI Practice/My_Pomodoro_Timer.py/tomato.png")
canvas.create_image(125, 112, image= tomato_img)
canvas.pack()




window.mainloop()