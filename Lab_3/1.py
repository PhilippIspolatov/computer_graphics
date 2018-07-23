from tkinter import *

from PIL import Image
def lighter(clr):
    cv = getcolor(clr)
    r,g,b = im.getpixel((0,0))
    print(r, g, b)

lighter("red")
