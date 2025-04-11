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
# month_names=[month_name[i] for i in range(1,13)]
# print(month_names)
# selected_month=tk.StringVar()
spinBox_vale=tk.StringVar()

# spinbox=ttk.Spinbox(root, values=[1,2,3,4,5,6,7,8,9,0], textvariable=spinBox_vale)
spinbox=ttk.Spinbox(root, from_=5,to=20,increment=2, textvariable=spinBox_vale)
spinbox.pack()

lable=ttk.Label(root,textvariable=spinBox_vale)
lable.pack()

root.mainloop()
