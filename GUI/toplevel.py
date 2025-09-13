from tkinter import *

top = Tk()
top.geometry("200x200")

def fun():
    child = Toplevel(top)   # Create a new window
    child.mainloop()

btn1 = Button(top, text="Open", width=10, command=fun)
btn1.place(x=50, y=50)

top.mainloop()
