from tkinter import *
from tkinter import messagebox
import numpy as np
import math as m
import os

mas_1 = []
mas_2 = []

def print_dots(mas_dots, color, koef, dx, dy, canvas):
	for i in mas_dots:
		canvas.create_oval(koef * i[0] - 2 + dx, 800 - koef * i[1] - 2 + dy, koef * i[0] + 2 + dx, 800 - koef * i[1] + 2 + dy, fill = color)
		canvas.create_text(koef * i[0] + 2 + dx, 800 - koef * i[1] + 2 + dy, text="(" + str(i[0]) + ";" + str(i[1]) + ")", font="Verdana 12",anchor="w",justify=CENTER,fill=color)


def length(x1, y1, x2, y2):
	return m.sqrt((y1 - y2)**2 + (x1 - x2)**2)

def check_tri(x1, y1, x2, y2, x3, y3):

	ab = length(x1, y1, x2, y2)
	bc = length(x2, y2, x3, y3)
	ac = length(x1, y1, x3, y3)

	return ((ab + bc - ac) > 0) and ((ab + ac - bc) > 0) and ((bc + ac - ab) > 0)

def print_circle(x1, y1, x2, y2, x3, y3, koef, dx, dy, canvas):
		if(check_tri(x1, y1, x2, y2, x3, y3)):

				c = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
				a = m.sqrt((x3 - x2)**2 + (y3 - y2)**2)
				b = m.sqrt((x3 - x1)**2 + (y3 - y1)**2)
			
				x0 = (a*x1 + b*x2 + c*x3)/(a + b + c)
				y0 = (a*y1 + b*y2 + c*y3)/(a + b + c)
				
				#canvas.create_line(koef * x1 + dx,800 - koef * y1 +dy,koef * x2 + dx,800 - koef * y2 + dy,width=3,fill="blue")
				#canvas.create_line(koef * x2 + dx,800 - koef * y2 +dy,koef * x3 + dx,800 - koef * y3 + dy,width=3,fill="blue")
				#canvas.create_line(koef * x3 + dx,800 - koef * y3 +dy,koef * x1 + dx,800 - koef * y1 + dy,width=3,fill="blue")

				return[x0, y0, x1, y1, x2, y2, x3, y3]


			

def check_input(string):

	res = True
	
	for word in string:
		if (word < "0" or word > "9"):
			if(word != " " and word != "." and word != "-"):
				res = False
	
	return res

x0 = 0
y0 = 0

def angle(x1, y1, x2, y2):
  
	talfa = abs(y2 - y1) / abs(x2 - x1)
	alfa = m.atan(talfa)

	return float(alfa)

def point(x1, y1, x2, y2, x3, y3):
	c = m.sqrt((x2-x1)**2 + (y2-y1)**2)
	a = m.sqrt((x3-x2)**2 + (y3-y2)**2)
	b = m.sqrt((x3-x1)**2 + (y3-y1)**2)

	x0 = (a*x1 + b*x2 + c*x3)/(a + b + c)
	y0 = (a*y1 + b*y2 + c*y3)/(a + b + c)

'''def lines(clear_cent, koef, dx, dy, canvas):

	mizer = 100
	min_i = 0
	min_j = 0
	
	if (len(clear_cent) != 0):
		for i in range(len(clear_cent)):
			for j in range(i, len(clear_cent)):
					if(clear_cent[i][0] - clear_cent[j][0] != 0 and clear_cent[i][1] - clear_cent[j][1] != 0):
							dot = angle(clear_cent[i][0], clear_cent[i][1], clear_cent[j][0], clear_cent[j][1])
							if(dot < mizer):
									min_i = i
									min_j = j
									mizer = dot
			
		if(min_i != None):						
			canvas.create_line(koef * clear_cent[min_i][0] + dx, 800 - koef * clear_cent[min_i][1] + dy, koef * clear_cent[min_j][0] + dx, 800 - koef * clear_cent[min_j][1] + dy, fill = "red")
			canvas.create_oval(koef * clear_cent[min_i][0] - 2 + dx, 800 - koef * clear_cent[min_i][1] - 2 + dy, koef * clear_cent[min_i][0] + 2 + dx, 800 - koef * clear_cent[min_i][1] + 2 + dy, fill = "black")
			canvas.create_oval(koef * clear_cent[min_j][0] - 2 + dx, 800 - koef * clear_cent[min_j][1] - 2 + dy, koef * clear_cent[min_j][0] + 2 + dx, 800 - koef * clear_cent[min_j][1]+ 2 + dy, fill = "black")
	
	return mizer'''

def lines(clear_cent_first, clear_cent_second, koef, dx, dy, canvas):

	mizer = 100
	min_i = 0
	min_j = 0
	
	if (len(clear_cent_first) != 0 and len(clear_cent_second) != 0 ):
		for i in range(len(clear_cent_first)):
			for j in range(len(clear_cent_second)):
					if(clear_cent_first[i][0] - clear_cent_second[j][0] != 0 and clear_cent_first[i][1] - clear_cent_second[j][1] != 0):
							dot = angle(clear_cent_first[i][0], clear_cent_first[i][1], clear_cent_second[j][0], clear_cent_second[j][1])
							if(dot < mizer):
									min_i = i
									min_j = j
									mizer = dot
			
		if(min_i != None and min_j != None):						
			canvas.create_line(koef * clear_cent_first[min_i][0] + dx, 800 - koef * clear_cent_first[min_i][1] + dy, koef * clear_cent_second[min_j][0] + dx, 800 - koef * clear_cent_second[min_j][1] + dy, fill = "red")
			canvas.create_oval(koef * clear_cent_first[min_i][0] - 2 + dx, 800 - koef * clear_cent_first[min_i][1]- 2 + dy, koef * clear_cent_first[min_i][0] + 2 + dx, 800 - koef * clear_cent_first[min_i][1] + 2 + dy, fill = "black")
			canvas.create_text(koef * clear_cent_first[min_i][0] + 2 + dx, 800 - koef * clear_cent_first[min_i][1] + 2 + dy, text="(" + str("%.4f" % clear_cent_first[min_i][0]) + ";" + str("%.4f" % clear_cent_first[min_i][1]) + ")", font="Verdana 12",anchor="w",justify=CENTER,fill="black")
			canvas.create_oval(koef * clear_cent_second[min_j][0] - 2 + dx, 800 - koef * clear_cent_second[min_j][1] - 2 + dy, koef * clear_cent_second[min_j][0] + 2 + dx, 800 - koef * clear_cent_second[min_j][1]+ 2 + dy, fill = "black")
			canvas.create_text(koef * clear_cent_second[min_j][0] + 2 + dx, 800 - koef * clear_cent_second[min_j][1] + 2 + dy, text="(" + str("%.4f" % clear_cent_second[min_j][0]) + ";" + str("%.4f" % clear_cent_second[min_j][1]) + ")", font="Verdana 12",anchor="w",justify=CENTER,fill="black")

			canvas.create_line(koef * clear_cent_first[min_i][2] + dx,800 - koef * clear_cent_first[min_i][3] +dy,koef * clear_cent_first[min_i][4] + dx,800 - koef * clear_cent_first[min_i][5] + dy,width=3,fill="blue")
			canvas.create_line(koef * clear_cent_first[min_i][4] + dx,800 - koef * clear_cent_first[min_i][5] +dy,koef * clear_cent_first[min_i][6] + dx,800 - koef * clear_cent_first[min_i][7] + dy,width=3,fill="blue")
			canvas.create_line(koef * clear_cent_first[min_i][6] + dx,800 - koef * clear_cent_first[min_i][7] +dy,koef * clear_cent_first[min_i][2] + dx,800 - koef * clear_cent_first[min_i][3] + dy,width=3,fill="blue")

			canvas.create_line(koef * clear_cent_second[min_j][2] + dx,800 - koef * clear_cent_second[min_j][3] +dy,koef * clear_cent_second[min_j][4] + dx,800 - koef * clear_cent_second[min_j][5] + dy,width=3,fill="blue")
			canvas.create_line(koef * clear_cent_second[min_j][4] + dx,800 - koef * clear_cent_second[min_j][5] +dy,koef * clear_cent_second[min_j][6] + dx,800 - koef * clear_cent_second[min_j][7] + dy,width=3,fill="blue")
			canvas.create_line(koef * clear_cent_second[min_j][6] + dx,800 - koef * clear_cent_second[min_j][7] +dy,koef * clear_cent_second[min_j][2] + dx,800 - koef * clear_cent_second[min_j][3] + dy,width=3,fill="blue")
	
	return mizer
		
def func(canvas, koef, dx, dy):
	
	data_1 = []
	with open("data_1.txt") as f:
		for line in f:
			data_1.append([float(x) for x in line.split()])
	f.close()

	ndata_1 = []


	
	for i in data_1:
		if i != None:
			ndata_1.append(i)

	data_2 = []
	with open("data_2.txt") as f:
		for line in f:
			data_2.append([float(x) for x in line.split()])

	ndata_2 = []
		
	for i in data_2:
		if i != None:
			ndata_2.append(i)
	f.close()
			
	mas_cent1 = []
	mas_cent2 = []

	for i in range(1, len(ndata_1)):
		for j in range(i):
			mas_cent1.append(print_circle(ndata_1[0][0], ndata_1[0][1], ndata_1[i][0], ndata_1[i][1], ndata_1[j][0], ndata_1[j][1], koef, dx, dy, canvas))

	for i in range(1, len(ndata_2)):
		for j in range(i):
			mas_cent2.append(print_circle(ndata_2[0][0], ndata_2[0][1], ndata_2[i][0], ndata_2[i][1], ndata_2[j][0], ndata_2[j][1], koef, dx, dy, canvas))
			
	clear_cent1 = []
	clear_cent2 = []

	for i in mas_cent1:
		if i != None:
			clear_cent1.append(i)


	for i in mas_cent2:
		if i != None:
			clear_cent2.append(i)


	print_dots(data_1, "red", koef, dx, dy, canvas)
	print_dots(data_2, "blue", koef, dx, dy, canvas)
	
	if((len(clear_cent1) >= 1) & (len(clear_cent2) >= 1)):
		canvas.create_text(100,50,text="Ответ: " + str("%.4f" % m.degrees(lines(clear_cent1, clear_cent2, koef, dx, dy, canvas))) + " градусов", font="Verdana 12",anchor="w",justify=CENTER,fill="red")




def change_1():
	global flag
	flag = "data_1.txt"

def change_2():
	global flag
	flag = "data_2.txt"

def refill():
	print(koef)
	main.delete("all")
	func(main, koef, dx, dy)
	root.update()



def add():

	if(check_input(message_add.get())):
		file = open(flag, "a")
		file.write(message_add.get() + "\n")
		file.close()
		refill()


def delete():

	if(check_input(message_del.get())):
		file = open(flag, "r")
		string = file.read()
		file.close()

		os.system("rm -rf " + flag)

		file = open(flag, "w")
		string = string.replace(message_del.get() + "\n", "")
		file.write(string)
		file.close()
		refill()


def clear():
	os.system("rm -rf " + flag)
	file = open(flag, "w")
	file.close()
	refill()

def mas_plus():
	global koef
	koef += 10
	refill()


def mas_minus():
	global koef
	koef -= 10
	refill()

def down():
	global dy
	dy += 20
	refill()

def up():
	global dy
	dy -= 20
	refill()

def right():
	global dx
	dx += 20
	refill()

def left():
	global dx
	dx -= 20
	refill()

size = 800
root = Tk()
main = Canvas(root, width=size, height=size)
main.pack()

koef = 60
flag = "data_1.txt"

dx = 0
dy = 0

refill()

bump = Tk()
bump.title("GUI на Python")
bump.geometry("500x400")

message_1 = IntVar()
message_2 = IntVar()

message_add = Entry(bump, textvariable=message_1)
message_add.place(relx=.7, rely=.1, anchor="c")
add_button = Button(bump, text = "ADD", command=add)
add_button.place(relx=.2, rely=.1, anchor="c")

message_del = Entry(bump, textvariable=message_2)
message_del.place(relx=.7, rely=.2, anchor="c")   
del_button = Button(bump, text="DEL", command=delete)
del_button.place(relx=.2, rely=.2, anchor="c")
	
clear_button = Button(bump, text="Clear", command=clear)
clear_button.place(relx=.2, rely=.3, anchor="c")

fst_data_button = Button(bump, text="First data", command=change_1)
fst_data_button.place(relx=.3, rely=.45, anchor="c")

scd_data_button = Button(bump, text="Second data", command=change_2)
scd_data_button.place(relx=.6, rely=.45, anchor="c")

plus_button = Button(bump, text="Plus", command=mas_plus)
plus_button.place(relx=.3, rely=.65, anchor="c")

minus_button = Button(bump, text="Minus", command=mas_minus)
minus_button.place(relx=.6, rely=.65, anchor="c")

up_button = Button(bump, text="UP", command=up)
up_button.place(relx=.45, rely=.87, anchor="c")

right_button = Button(bump, text="RIGHT", command=right)
right_button.place(relx=.6, rely=.95, anchor="c")

down_button = Button(bump, text="DOWN", command=down)
down_button.place(relx=.45, rely=.95, anchor="c")

left_button = Button(bump, text="LEFT", command=left)
left_button.place(relx=.3, rely=.95, anchor="c")

bump.mainloop()
