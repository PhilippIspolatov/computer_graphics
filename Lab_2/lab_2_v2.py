from tkinter import *
from tkinter import messagebox
from copy import *
import math as m

global mas
mas = []
global b_mas
b_mas  = []

def cir(mas, fr, to):
    y = fr
    
    while (y <= to): 
        mas.append([float(m.sqrt(16 - y**2)), float(y)])
        mas.append([float(y**2), float(y)])
        y += 0.001

cir(mas, -1.888, 1.888)


def print_figure():
    main.delete("all")
    for dot in mas:
        main.create_oval(dot[0] * 50 - 1 + 100, dot[1] * 50 - 1 + 100, dot[0] * 50 + 1 + 100, dot[1] * 50 + 1 + 100, fill = "black")

size = 800
root = Tk()
main = Canvas(root, width=size, height=size)
main.pack()

print_figure()


def rotate():
  
    angle = m.radians(float(message_angle.get()))
    x = float(message_x.get())
    y = float(message_y.get())

    b_mas = mas

    for i in range(len(mas)):
        n_x = x + (mas[i][0] - x) * m.cos(angle) + (mas[i][1] - y) * m.sin(angle)
        n_y = y + (mas[i][1] - y) * m.cos(angle) - (mas[i][0] - x) * m.sin(angle)
        mas[i][0] = n_x
        mas[i][1] = n_y


    print_figure()


def scale():

    koef_x = float(message_koef_x.get())
    koef_y = float(message_koef_y.get())
    xm = float(message_xm.get())
    ym = float(message_ym.get())

    b_mas = mas


    for dot in mas:
        dot[0] = dot[0] + koef_x * (dot[0] - xm)
        dot[1] = dot[1] + koef_y * (dot[1] - ym)


    print_figure()
	
def replace():

    lb_mas = []
    dx = float(message_dx.get())
    dy = float(message_dy.get())

    print(mas[0])
    b_mas = deepcopy(mas)
    
    '''for dot in mas:
        b_mas.append(dot)
    print(b_mas[0][0], b_mas[0][1])'''

    for dot in mas:
        dot[0] += dx
        dot[1] += dy

    print(mas[0][0], mas[0][1])
    print(b_mas[0][0], b_mas[0][1])
    print_figure()


def back():
    print("!!!")
    print(mas[0][0])
    print(b_mas[0][0])
    mas = deepcopy(b_mas)
    print(mas[0])
    print_figure()
    
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()


message_1 = DoubleVar()
message_2 = DoubleVar()

message_dx = Entry(canvas, textvariable=message_1)
message_dx.place(relx=.7, rely=.1, anchor="c")
message_dy = Entry(canvas, textvariable=message_2)
message_dy.place(relx=.7, rely=.2, anchor="c")   
replace_button = Button(canvas, text = "REPLACE", command=replace)
replace_button.place(relx=.2, rely=.1, anchor="c")
canvas.create_text(40, 10, text="dx = ", font="Verdana 12",anchor="w",justify=CENTER,fill="black")

x = DoubleVar()
y = DoubleVar()
angle = DoubleVar()

message_x = Entry(canvas, textvariable=x)
message_x.place(relx=.7, rely=.3, anchor="c")
message_y = Entry(canvas, textvariable=y)
message_y.place(relx=.7, rely=.4, anchor="c") 
message_angle = Entry(canvas, textvariable=angle)
message_angle.place(relx=.7, rely=.5, anchor="c")  
rotate_button = Button(canvas, text = "ROTATE", command=rotate)
rotate_button.place(relx=.2, rely=.3, anchor="c") 

xm = DoubleVar()
ym = DoubleVar()
koef_x = DoubleVar()
koef_y = DoubleVar()

message_xm = Entry(canvas, textvariable=xm)
message_xm.place(relx=.7, rely=.6, anchor="c")
message_ym = Entry(canvas, textvariable=ym)
message_ym.place(relx=.7, rely=.7, anchor="c") 
message_koef_x = Entry(canvas, textvariable=koef_x)
message_koef_x.place(relx=.7, rely=.8, anchor="c")  
message_koef_y = Entry(canvas, textvariable=koef_y)
message_koef_y.place(relx=.7, rely=.9, anchor="c") 
scale_button = Button(canvas, text = "SCALE", command=scale)
scale_button.place(relx=.2, rely=.6, anchor="c")

rotate_button = Button(canvas, text = "BACKWARD", command=back)
rotate_button.place(relx=.2, rely=.9, anchor="c") 

root.mainloop()
