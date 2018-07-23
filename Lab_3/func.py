from tkinter import *
from numpy import *
from tkinter import messagebox
import math as m

def glush():
    print(1 + 1)
    return 0


def cda():
    
    print(clr)
    xn = int(message_xn.get())
    yn = int(message_yn.get())
    xk = int(message_xk.get())
    yk = int(message_yk.get())
    if ((xn == xk) and (yn == yk)):
        main.create_oval(xn, yn, xn, yn, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = xk - xn
    dy = yk - yn
    if (abs(dx) > abs(dy)):
        L = abs(dx)
    else:
        L = abs(dy)
    dx = dx / L
    dy = dy / L
    for i in range(1, L + 1):
        main.create_oval(xt, yt, xt, yt, outline=clr, fill=clr)
        xt += dx
        yt += dy
    return 0


def float_brez():
    xn = int(message_xn.get())
    yn = int(message_yn.get())
    xk = int(message_xk.get())
    yk = int(message_yk.get())
    if ((xn == xk) and (yn == yk)):
        main.create_oval(xn, yn, xn, yn, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = xk - xn
    dy = yk - yn
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if (dx < dy):
        fl = 1
        t = dy
        dy = dx
        dx = t
    else:
        fl = 0
    m = dy / dx
    e = m - 0.5
    for i in range(1, dx + 1):
        main.create_oval(xt, yt, xt, yt, outline=clr, fill=clr)
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


def int_brez():
    global clr
    xn = int(message_xn.get())
    yn = int(message_yn.get())
    xk = int(message_xk.get())
    yk = int(message_yk.get())
    print(clr)
    if ((xn == xk) and (yn == yk)):
        print(clr)
        main.create_oval(xn, yn, xn, yn, fill=clr, outline=clr)
        return 0
    xt = xn
    yt = yn
    dx = xk - xn
    dy = yk - yn
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if (dx < dy):
        fl = 1
        t = dy
        dy = dx
        dx = t
    else:
        fl = 0
    e = 2 * dy - dx
    for i in range(1, dx + 1):
        main.create_oval(xt, yt, xt, yt, outline=clr, fill=clr)
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


def std():
    xn = int(message_xn.get())
    yn = int(message_yn.get())
    xk = int(message_xk.get())
    yk = int(message_yk.get())
    print(clr)
    main.create_line(xn, yn, xk, yk, fill="%80red")
    return 0


def withoutstep():
    return 0


def setcolor(col):
    global clr
    clr = col
    print(clr)
    return 0


def create_screen(color):
    size = 800
    root = Tk()
    global main
    main = Canvas(root, width=size, height=size, bg=color)
    main.pack()
    return 0

print("OK")
