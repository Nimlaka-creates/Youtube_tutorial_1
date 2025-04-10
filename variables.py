# variables
#library
import tkinter as tk
from tkinter import ttk 
root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('300x200')
root.resizable(False,True)
# //////////////////////////////////////////////////////////////////////////////////////////

# variable initialization
variable_value = tk.StringVar(value='Welcome')

# lable
lable = ttk.Label(root, textvariable=variable_value)
lable.pack()

# entry field
entry = ttk.Entry(root, textvariable=variable_value)
entry.pack()

# button
button = ttk.Button(root, text='click_me', command=lambda:print(variable_value.get()))
button.pack()

root.mainloop()
