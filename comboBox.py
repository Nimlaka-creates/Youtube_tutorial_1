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
month_names=[month_name[i] for i in range(1,13)]
print(month_names)
selected_month=tk.StringVar()

combo_box=ttk.Combobox(root, values=month_names, textvariable=selected_month)
combo_box.pack()

lable=ttk.Label(root, textvariable=selected_month)
lable.pack()



root.mainloop()
