from tkinter import *
from tkinter import messagebox

# Create main window
top = Tk()
top.geometry("300x200")

# Function for blue button
def fun():
    messagebox.showinfo("Hello", "Blue button clicked")

# Red button
btn1 = Button(top, text="Red", bg="red", fg="white", width=10)
btn1.pack(side=LEFT)

# Green button
btn2 = Button(top, text="Green", bg="green", fg="white", width=10, height=5)
btn2.pack(side=TOP)

# Blue button (with function)
btn3 = Button(top, text="Blue", bg="blue", fg="white", padx=10, pady=10, command=fun)
btn3.pack(side=BOTTOM)

# Run the window
top.mainloop()
