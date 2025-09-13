from tkinter import *

top = Tk()
top.geometry("300x200")

# Listbox for colours
lb = Listbox(top, height=5, fg="red", bg="yellow")
lb.place(x=10, y=30)

lb.insert(1, "Red")
lb.insert(2, "Yellow")
lb.insert(3, "Green")
lb.insert(4, "Blue")

# Label for fruits
lb2 = Label(top, text="List of fruits", fg="blue", bg="red")
lb2.place(x=150, y=10)

# Listbox for fruits
lb1 = Listbox(top)
lb1.place(x=160, y=30)

lb1.insert(1, "Mango")
lb1.insert(2, "Grapes")
lb1.insert(3, "Banana")
lb1.insert(4, "Berry")

top.mainloop()


'''
✅ This will create:

A Listbox of colours (Red, Yellow, Green, Blue)

A Label that says “List of fruits”

A Listbox of fruits (Mango, Grapes, Banana, Berry)
'''