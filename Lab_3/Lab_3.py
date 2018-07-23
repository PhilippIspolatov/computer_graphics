from tkinter import *
from numpy import *
from tkinter import messagebox
from tkinter import colorchooser
import math as m
 
FLAG = 0
size = 800
clr = '#000000'
clr_rgb = [00, 00, 00]
color = '#ffffff'
color_rgb = [255, 255, 255]

but = Tk()
canvas = Canvas(but, width=500, height=500)
canvas.pack()

def glush():
    print(1 + 1)
    return 0


def cda(four_koord):

    global FLAG 
    FLAG = 1

    xn = int(four_koord[0])
    yn = int(four_koord[1])
    xk = int(four_koord[2])
    yk = int(four_koord[3])
    
    #print(clr)
    if ((xn == xk) and (yn == yk)):
        main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = int(xk - xn)
    dy = int(yk - yn)
    if (abs(dx) > abs(dy)):
        L = int(abs(dx))
    else:
        L = int(abs(dy))
    sx = dx / L
    sy = dy / L
    for i in range(1, L + 1):
        #print("CDA:  " + str(round(xt)) + "  " + str(round(yt)))
        main.create_oval(round(xt), round(yt), round(xt), round(yt), width = 0, outline=clr, fill=clr)
        xt += sx
        yt += sy
    return 0


def float_brez(four_koord):

    global FLAG
    FLAG = 2
    xn = int(four_koord[0])
    yn = int(four_koord[1])
    xk = int(four_koord[2])
    yk = int(four_koord[3])
    if ((xn == xk) and (yn == yk)):
        main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = int(xk - xn)
    dy = int(yk - yn)
    sx = int(sign(dx))
    sy = int(sign(dy))
    dx = int(abs(dx))
    dy = int(abs(dy))
    if (dx < dy):
        fl = 1
        t = dy
        dy = dx
        dx = int(t)
    else:
        fl = 0
    m = dy / dx
    e = m - 0.5
    for i in range(1, dx + 1):
        #print("BREZ:  " + str(xt) + "  " + str(yt))
        main.create_oval(round(xt), round(yt), round(xt), round(yt), width = 0, outline=clr, fill=clr)
        if (e >= 0):
            if (fl == 0):
                yt = yt + sy
            else:
                xt = xt + sx
            e = e - 1

        if (fl == 0):
            xt = xt + sx
        else:
            yt = yt + sy
        e = e + m

    return 0


def int_brez(four_koord):

    global FLAG
    FLAG = 3
    
    global clr
    xn = int(four_koord[0])
    yn = int(four_koord[1])
    xk = int(four_koord[2])
    yk = int(four_koord[3])
    #print(clr)
    if ((xn == xk) and (yn == yk)):
        #print(clr)
        main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = xk - xn
    dy = yk - yn
    sx = int(sign(dx))
    sy = int(sign(dy))
    dx = int(abs(dx))
    dy = int(abs(dy))
    if (dx < dy):
        fl = 1
        t = dy
        dy = dx
        dx = t
    else:
        fl = 0
    e = 2 * dy - dx
    for i in range(1, dx + 1):
        main.create_oval(xt, yt, xt, yt, width = 0, outline=clr, fill=clr)
        if (e >= 0):
            if (fl == 0):
                yt = yt + sy
            else:
                xt = xt + sx
            e = e - 2 * dx
        if (fl == 0):
            xt = xt + sx
        else:
            yt = yt + sy
        e = e + 2 * dy


    return 0


def std(four_koord):
    global FLAG
    FLAG = 5
    xn = int(four_koord[0])
    yn = int(four_koord[1])
    xk = int(four_koord[2])
    yk = int(four_koord[3])
    #print(clr)
    main.create_line(xn, yn, xk, yk, fill=clr)
    return 0


def withoutstep(four_koord):
    
    global FLAG
    FLAG = 4
    global clr
    xn = int(four_koord[0])
    yn = int(four_koord[1])
    xk = int(four_koord[2])
    yk = int(four_koord[3])
    if ((xn == xk) and (yn == yk)):
        main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = xk - xn
    dy = yk - yn
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    fl = 0
    if (dx == 0):
        m = 1
    else:
        m = dy / dx
    i_max = 100
    if (dy > dx):
        dx = dy
        m = 1 / m
        fl = 1
    else:
        fl = 0
    m = m * i_max
    e = 1 / 2
    w = i_max - m

    clr = lighter(round(i_max / 2))
    #print('>>' + str(clr))
    main.create_oval(xt, yt, xt ,yt, width = 0, fill=clr, outline=clr)

    for i in range(1, dx + 1):
        if (e <= w):
            if (fl == 1):
                yt = yt+ sy
            else:
                xt = xt + sx
            e = e + m
        else:
            xt = xt + sx
            yt = yt + sy

            e = e - w
        #print(clr)
        clr = lighter(round(e))
        #print(clr)
        main.create_oval(xt, yt, xt, yt, width = 0, fill=clr, outline=clr)
   
    return 0

def val():
    return [int(message_xn.get()), int(message_yn.get()), int(message_xk.get()), int(message_yk.get())]


def line_br_smooth(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    win.pen.setColor(win.color_line)
    dx = xk - xn
    dy = yk - yn
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = xn
    y = yn

    try:
        h = dy / dx
    except ZeroDivisionError:
        h = 0


    isBlack = False

    if win.pen.color() == Qt.black:
        i_max = 256
        isBlack = True
    else:
        i_max = 100

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True
        if h:
            h = 1 / h

    h *= i_max
    e = i_max/2
    w = i_max - h
    i = 1
    while i <= dx:
        if not isBlack:
            new = win.pen.color()
            new.lighter(100 + e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        else:
            new = QColor()
            new.setRgb(0, 0, 0, alpha=255 - e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i += 1

def lighter(intensivity):
    color_r = clr_rgb[0] + (color_rgb[0] - clr_rgb[0])*intensivity/100
    color_g = clr_rgb[1] + (color_rgb[1] - clr_rgb[1])*intensivity/100
    color_b = clr_rgb[2] + (color_rgb[2] - clr_rgb[2])*intensivity/100

    return '#' + to_16(int(color_r)) + to_16(int(color_g)) + to_16(int(color_b))

def to_16(x):
    string = str(hex(x)[-2:])
    if (string[len(string) - 2] == "x"):
        string = "0" + string[-1:]
    return string[-2:]

    


def setcolor(col):
    global clr
    global clr_rgb
    clr = col
    if(clr == "#000000"):
        clr_rgb = [00, 00, 00]
    if (clr == "#ffffff"):
        clr_rgb = [255, 255, 255]
    if (clr == "#00ff00"):
        clr_rgb = [00, 255, 00]
    #print(clr)
    return 0


def create_screen(color):
    global color_rgb
    if(color == "#000000"):
        color_rgb = [00, 00, 00]
    if (color == "#ffffff"):
        color_rgb = [255, 255, 255]
    if (color == "#00ff00"):
        color_rgb = [00, 255, 00]
    
    root = Tk()
    global main
    main = Canvas(root, width=size, height=size, bg=color)
    main.pack()
    return 0

def star():
    angle = int(message_ang.get())
    lenght = int(message_len.get())

    gtr = pi / 180

    x = size / 2
    y = size / 2

    i = angle

    while ((i <= 360) and (i >= -360)):
        w = round(lenght * sin((90 - i) * gtr))
        h = round(lenght * sin(i * gtr))

        xk = x + w
        yk = y - h

        mas = [x, y, xk, yk]

        #print(mas)

        if (FLAG == 1):
            cda(mas)
        elif (FLAG == 2):
            float_brez(mas)
        elif (FLAG == 3):
            int_brez(mas)
        elif (FLAG == 4):
            withoutstep(mas)
        elif (FLAG == 5):
            std(mas)
        i = i + angle;

        #print(FLAG)

    return 0

def delit(main):
    main.delete("all")

message_1 = IntVar()
message_2 = IntVar()
message_3 = IntVar()
message_4 = IntVar()
message_5 = IntVar()
message_6 = IntVar()

message_xn = Entry(but, textvariable=message_1)
message_xn.place(relx=.7, rely=.1, anchor="c")
message_yn = Entry(but, textvariable=message_2)
message_yn.place(relx=.7, rely=.2, anchor="c")
canvas.create_text(220, 50, text="x_n", font="Verdana 12", anchor="w", justify=CENTER, fill="black")
canvas.create_text(220, 100, text="y_n", font="Verdana 12", anchor="w", justify=CENTER, fill="black")

message_xk = Entry(but, textvariable=message_3)
message_xk.place(relx=.7, rely=.3, anchor="c")
message_yk = Entry(but, textvariable=message_4)
message_yk.place(relx=.7, rely=.4, anchor="c")
canvas.create_text(220, 150, text="x_k", font="Verdana 12", anchor="w", justify=CENTER, fill="black")
canvas.create_text(220, 200, text="y_k", font="Verdana 12", anchor="w", justify=CENTER, fill="black")

one_button = Button(but, text="CDA", command=lambda: cda(val()))
one_button.place(relx=.1, rely=.8, anchor="c")
two_button = Button(but, text="FLOAT", command=lambda: float_brez(val()))
two_button.place(relx=.3, rely=.8, anchor="c")
three_button = Button(but, text="INT", command=lambda: int_brez(val()))
three_button.place(relx=.5, rely=.8, anchor="c")
four_button = Button(but, text="NO STEP", command=lambda: withoutstep(val()))
four_button.place(relx=.7, rely=.8, anchor="c")
five_button = Button(but, text="STD", command=lambda: std(val()))
five_button.place(relx=.9, rely=.8, anchor="c")

black_button = Button(but, text="Black screen", command=lambda: create_screen("#000000"))
black_button.place(relx=.2, rely=.6, anchor="c")
white_button = Button(but, text="White screen", command=lambda: create_screen("#ffffff"))
white_button.place(relx=.5, rely=.6, anchor="c")
green_button = Button(but, text="Green screen", command=lambda: create_screen("#00ff00"))
green_button.place(relx=.8, rely=.6, anchor="c")

black_button = Button(but, text="Black line", command=lambda: setcolor("#000000"))
black_button.place(relx=.2, rely=.7, anchor="c")
black_button = Button(but, text="White line", command=lambda: setcolor("#ffffff"))
black_button.place(relx=.5, rely=.7, anchor="c")
black_button = Button(but, text="Green line", command=lambda: setcolor("#00ff00"))
black_button.place(relx=.8, rely=.7, anchor="c")

star_button = Button(but, text="*", command=star)
star_button.place(relx=.7, rely=.9, anchor="c")

message_ang = Entry(but, textvariable=message_5)
message_ang.place(relx=.2, rely=.1, anchor="c")
message_len = Entry(but, textvariable=message_6)
message_len.place(relx=.2, rely=.2, anchor="c")

black_button = Button(but, text="CLEAR", command = lambda: delit(main))
black_button.place(relx=.4, rely=.9, anchor="c")

but.mainloop()
main.mainloop()
