from tkinter import *
from tkinter import messagebox
import math as m

pre_mas = []
mas = []

size = 800
koef = 25


def cir(fr, to):
    y = fr
    
    while (y <= to): 
        mas.append([float(m.sqrt(16 - y**2) * koef + size/2), float(y) * koef + size/2])
        mas.append([float(y**2) * koef + size/2 , float(y) * koef + size/2])
        y += 0.001

def print_figure():
    main.delete("all")
    for dot in mas:
        main.create_oval(dot[0] - 1, dot[1] - 1, dot[0] + 1, dot[1] + 1, fill = "black")


def rotate():
    global pre_mas
    pre = []

    for i in mas:
        pre.append([i[0], i[1]])

    pre_mas = mas
  
    angle = m.radians(float(message_angle.get()))
    x = float(message_x.get()) + size / 2
    y = float(message_y.get()) + size / 2

    for i in range(len(mas)):
        n_x = x + (mas[i][0] - x) * m.cos(angle) + (mas[i][1] - y) * m.sin(angle)
        n_y = y + (mas[i][1] - y) * m.cos(angle) - (mas[i][0] - x) * m.sin(angle)
        mas[i][0] = n_x
        mas[i][1] = n_y

    pre_mas = pre

    print_figure()


'''def scale():

    global pre_mas
    pre = []

    for i in mas:
        pre.append([i[0], i[1]])

    pre_mas = mas

    koef_x = float(message_koef_x.get())
    koef_y = float(message_koef_y.get())
    xm = float(message_xm.get())
    ym = float(message_ym.get())


    for dot in mas:
        dot[0] = dot[0] + koef_x * (dot[0] - xm)
        dot[1] = dot[1] + koef_y * (dot[1] - ym)

    pre_mas = pre

    print_figure()'''


def scale():

    global pre_mas
    pre = []

    for i in mas:
        pre.append([i[0], i[1]])

    pre_mas = mas

    koef_x = float(message_koef_x.get())
    koef_y = float(message_koef_y.get()) 
    xm = float(message_xm.get()) + size / 2
    ym = float(message_ym.get()) + size / 2

    #print(mas[0])


    for dot in mas:
        dot[0] = round(dot[0] * koef_x + (1 - koef_x) * xm)
        dot[1] = round(dot[1] * koef_y + (1 - koef_y) * ym)

    #print(mas[0])  

    pre_mas = pre

    print_figure()
	

def replace():

    global pre_mas
    pre = []

    for i in mas:
        pre.append([i[0], i[1]])

    dx = float(message_dx.get())
    dy = float(message_dy.get())

    for i in range(len(mas)):
        mas[i][0] += dx
        mas[i][1] += dy

    pre_mas = pre

    print_figure()

def undo():
    global mas, pre_mas

    mas = pre_mas
    print_figure()


size = 800
root = Tk()
main = Canvas(root, width=size, height=size)
main.pack()

cir(-1.888, 1.888)
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

undo_button = Button(canvas, text = "undo", command=undo)
undo_button.place(relx=.7, rely=.95, anchor="c")

canvas.create_text(140,40, text="dx", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,80, text="dy", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,120, text="x", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,160, text="y", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,200, text="angle", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,240, text="x", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,280, text="y", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,320, text="koef_x", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
canvas.create_text(140,360, text="koef_y", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
root.mainloop()
