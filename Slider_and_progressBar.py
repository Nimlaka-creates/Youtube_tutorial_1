#library
import tkinter as tk
from tkinter import ttk 
from calendar import month_name

root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('300x200')
root.resizable(False,True)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////

scale_value= tk.DoubleVar(value=100)
scale = ttk.Scale(root,command=lambda value:print(value), from_=0,to=100,length=300,variable=scale_value)
scale.pack()

progressBar = ttk.Progressbar(root, variable=scale_value)
progressBar.pack()
root.mainloop()
