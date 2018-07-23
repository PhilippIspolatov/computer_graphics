from time import *
from tkinter import *
from numpy import *
from tkinter import messagebox
from tkinter import colorchooser
import math as m
import matplotlib.pyplot as plt
import numpy as np

clr = '#000000'
clr_rgb = [00, 00, 00]
color_rgb = [255, 255, 255]
col = 5
time = []
xn = 10
yn = 10
xk = 200
yk = 200

def cda():
    
    if ((xn == xk) and (yn == yk)):
        #main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
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
        #main.create_oval(xt, yt, xt, yt, width = 0, outline=clr, fill=clr)
        xt += dx
        yt += dy
    return 0


def float_brez():
    if ((xn == xk) and (yn == yk)):
        #main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
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
        #main.create_oval(xt, yt, xt, yt, width = 0, outline=clr, fill=clr)
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
    #print(clr)
    if ((xn == xk) and (yn == yk)):
        #print(clr)
        #main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
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
        #main.create_oval(xt, yt, xt, yt, width = 0, outline=clr, fill=clr)
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
    print(clr)
    #main.create_line(xn, yn, xk, yk, fill='red80')
    return 0

def to_16(x):
    string = str(hex(x)[-2:])
    if (string[len(string) - 2] == "x"):
        string = "0" + string[-1:]
    return string[-2:]

def lighter(intensivity):
    color_r = clr_rgb[0] + (color_rgb[0] - clr_rgb[0])*intensivity/100
    color_g = clr_rgb[1] + (color_rgb[1] - clr_rgb[1])*intensivity/100
    color_b = clr_rgb[2] + (color_rgb[2] - clr_rgb[2])*intensivity/100

    return '#' + to_16(int(color_r)) + to_16(int(color_g)) + to_16(int(color_b))


def withoutstep():
    global clr
    if ((xn == xk) and (yn == yk)):
        #print(clr)
        #main.create_oval(xn, yn, xn, yn, width = 0, fill=clr, outline=clr)
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
        clr = lighter(round(e))
   
    return 0



tt = 0
for i in range(1,col):
    start_time = clock()    
    cda()
    tt += clock() - start_time
tt = tt / col
time.append(tt)

tt = 0
for i in range(1,col):
    start_time = clock()    
    float_brez()
    tt += clock() - start_time
tt = tt / col
time.append(tt)

tt = 0
for i in range(1,col):
    start_time = clock()    
    int_brez()
    tt += clock() - start_time
tt = tt / col
time.append(tt)

tt = 0
for i in range(1,col):
    start_time = clock()    
    std()
    tt += clock() - start_time
tt = tt / col
time.append(tt)

tt = 0
for i in range(1,col):
    start_time = clock()    
    withoutstep()
    tt += clock() - start_time
tt = tt / col
time.append(tt)

print(time)

data1=time[0]
data2=time[1]
data3=time[2]
data4=time[3]
data5=time[4]

locs = np.arange(0,1)
mas = ("DDA", "Brez. Float", "Brez. Int", "Standart", "No steps")
width = 0.1

plt.bar(locs, data1, width=width)
plt.bar(locs+width, data2, width=width, color='red')
plt.bar(locs+2*width, data3, width=width, color='green')
plt.bar(locs+3*width, data4, width=width, color='yellow')
plt.bar(locs+4*width, data5, width=width, color='blue')

plt.xticks(locs + width*10, locs)

plt.xlabel("Methods")
plt.ylabel("Time/secs")
plt.legend(mas)
plt.show()
    
