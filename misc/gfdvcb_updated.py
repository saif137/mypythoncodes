##http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

##https://www.tutorialspoint.com/python/tk_entry.htm
##http://effbot.org/tkinterbook/entry.htm

##import tkinter
##root = tkinter.Tk(  )
##for r in range(9):
##    for c in range(9):
##        tkinter.Label(root, text='R%s/C%s'%((r+1),(c+1)),
##            borderwidth=10 ).grid(row=r,column=c)
##root.mainloop(  )


##from tkinter import *
##
##root = Tk()
##
##w = Label(root, text="Red Sun", bg="red", fg="white")
##w.pack(fill=X,ipadx=100)
##w = Label(root, text="Green Grass", bg="green", fg="black")
##w.pack(fill=X,padx=50)
##w = Label(root, text="Blue Sky", bg="blue", fg="white")
##w.pack(fill=X)
##
##mainloop()
##


# using the Tkinter canvas to
# draw a line from coordinates x1,y1 to x2,y2
# create_line(x1, y1, x2, y2, width=1, fill="black")
#

def key(event):
   print ("pressed", repr(event.char))

def callback(event):
   frame.focus_set()
   print ("clicked at", event.x, event.y)

import Tkinter as tk
from Tkinter import Button
from Tkinter import *
root = tk.Tk()
root.title("Sudoku")
frame = tk.Frame(root, width=100, height=100)
b = Button(frame, text='1', padx = 2)
b.pack(pady = 5, padx = 2)
frame.pack()

# create the drawing canvas
canvas = tk.Canvas(frame, width=450, height=450, bg='gray89')
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
# draw horizontal lines
x1 = 0
x2 = 450

for k in range(0, 500, 50):
    y1 = k
    y2 = k
    canvas.create_line(x1, y1, x2, y2,  fill="black", dash=(4, 4))
for k in range(0, 500, 150):
    y1 = k
    y2 = k
    canvas.create_line(x1, y1, x2, y2,  fill="black")
# draw vertical lines
y1 = 0
y2 = 450
for k in range(0, 500, 50):
    x1 = k
    x2 = k
    canvas.create_line(x1, y1, x2, y2, fill="black", dash=(4,4))
for k in range(0, 500, 150):
    x1 = k
    x2 = k
    canvas.create_line(x1, y1, x2, y2,  fill="black")

root.mainloop()