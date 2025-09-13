#This code creates a Tkinter window with three labels (Name, Password, Age), each styled differently with colors, padding, and positions.
from tkinter import *

# Create main window
top = Tk()
top.geometry("300x200")

# Label 1 - simple text
lbl1 = Label(top, text="Name")
lbl1.place(x=10, y=10)

# Label 2 - styled with foreground & background
lbl2 = Label(top, text="Password", fg="red", bg="yellow")
lbl2.place(x=10, y=40)

# Label 3 - styled with padding and background
lbl3 = Label(top, text="Age", padx=10, pady=10, bg="green")
lbl3.place(x=10, y=70)

# Run the window
top.mainloop()
