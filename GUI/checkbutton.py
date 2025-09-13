#This code creates a Tkinter window with three checkboxes (Red, Green, Blue) having different text and background styles.
from tkinter import *

# Create main window
top = Tk()
top.geometry("300x200")

# Red Checkbutton
chkbtn1 = Checkbutton(top, text="Red", fg="red")
chkbtn1.pack()

# Green Checkbutton with active color
chkbtn2 = Checkbutton(top, text="Green", fg="green", activebackground="yellow")
chkbtn2.pack()

# Blue Checkbutton with background orange
chkbtn3 = Checkbutton(top, text="Blue", fg="blue", bg="orange", width=10)
chkbtn3.pack()

# Run the window
top.mainloop()
