from tkinter import *
from tkinter import messagebox
import math as m
mas = []
def cir(mas, fr, to):
    y = fr
    
    while (y <= to):
        lmas = []
        lmas.append(float(y))
        lmas.append(float(m.sqrt(16 - y**2)))
        lmas.append(float(y**2))
        mas.append(lmas)
        y += 0.001

cir(mas, -1.888, 1.888)

def print(canvas, mas):
    for i in range(0, len(mas)):
        canvas.create_oval(mas[i][2] * 10 - 1 + 100, mas[i][0] * 10 - 1 + 100, mas[i][2] * 10  + 100, mas[i][0] * 10 + 100, fill = "black")
        canvas.create_oval(mas[i][1] * 10 - 1 + 100, mas[i][0] * 10 - 1 + 100, mas[i][1] * 10 + 100, mas[i][0] * 10 + 100, fill = "black")
        

size = 800
root = Tk()
main = Canvas(root, width=size, height=size)
main.pack()

root.mainloop()

print(main, mas)
	
def replace():
    dx = int(message_dx.get())
    dy = int(message_dy.get())
    for i in range(0, len(mas)):
        mas[i][2] += dx
        mas[i][1] += dx
        mas[i][0] += dy
    print(main, mas)
    

bump = Tk()
bump.title("GUI на Python")
bump.geometry("500x400")

message_1 = IntVar()
message_2 = IntVar()

message_dx = Entry(bump, textvariable=message_1)
message_dx.place(relx=.7, rely=.1, anchor="c")
message_dy = Entry(bump, textvariable=message_2)
message_dy.place(relx=.7, rely=.2, anchor="c")

replace_button = Button(bump, text = "REPLACE", command=replace())
replace_button.place(relx=.2, rely=.1, anchor="c")

bump.mainloop()
bump.pack()

