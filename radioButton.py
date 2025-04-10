#library

import tkinter as tk
from tkinter import ttk 
root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('300x200')
root.resizable(False,True)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
radio_var = tk.StringVar()
def select_radio():
    lable.configure(text=radio_var.get())

radio1=ttk.Radiobutton(root, text='Python',value='Python',variable=radio_var,command=select_radio)
radio1.pack()

radio2=ttk.Radiobutton(root, text='Java',value='Java',variable=radio_var,command=select_radio)
radio2.pack()

radio3=ttk.Radiobutton(root, text='C++', value='C++',variable=radio_var,command=select_radio)
radio3.pack()

lable=ttk.Label(root)
lable.pack()

root.mainloop()
