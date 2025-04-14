#library
import tkinter as tk
from tkinter import ttk 
from calendar import month_name

root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('800x800')
root.resizable(True,True)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

frame1=ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame1.pack_propagate(False)

frame1.pack(side='bottom')

entry=ttk.Entry(frame1)
entry.pack(pady=10)

button=ttk.Button(frame1, text='Submit')
button.pack()

frame2=ttk.Frame(root, width=200, height=600, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

lable=ttk.Label(frame2, text='WELCOME')
lable.pack()

button2=ttk.Button(frame2,text='Click me')
button2.pack()


root.mainloop()
