import tkinter as tk
#from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
def show_pie_chart():
    v1 = 35
    v2 = 25
    v3 = 25
    v4 = 15
    y = np.array([v1, v2, v3, v4])
    
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    
    plt.pie(y, labels = mylabels)
    plt.show()
top = tk.Tk()
top.title("Show Pie Chart")
top.geometry("400x300")
#btn1 = Button(top, text = "Login")
#btn1.pack(side = TOP)
btn = tk.Button(top, text="Show Pie Chart", command=show_pie_chart)
btn.pack(pady=50)

top.mainloop()