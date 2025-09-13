#This code creates a Tkinter window with three text boxes — a normal entry, a yellow background entry, and a password entry where typed text is hidden with *.

from tkinter import *

# Create main window
top = Tk()
top.geometry("300x200")

# Normal Entry (text box)
entry0 = Entry(top, width=30)
entry0.place(x=50, y=40)

# Entry with yellow background
entry1 = Entry(top, bg="yellow")
entry1.place(x=50, y=70)

# Entry for password (red text, hidden with '*')
entry2 = Entry(top, fg="red", show="*")
entry2.place(x=50, y=100)

# Run the window
top.mainloop()
