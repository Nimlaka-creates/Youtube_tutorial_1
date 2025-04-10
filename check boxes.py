# checkboxes
#library

import tkinter as tk
from tkinter import ttk 
root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('300x200')
root.resizable(False,True)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
chkbox_values=[tk.StringVar(),tk.StringVar()]
lable_var=tk.StringVar()

def checkbox_result():
    output_var="Select languages: "+ chkbox_values[0].get() +" "+ chkbox_values[1].get()
    lable_var.set(output_var)
    
check1 =ttk.Checkbutton(root, text='Python', variable=chkbox_values[0], onvalue='Python',offvalue='')
check1.pack()

check2 =ttk.Checkbutton(root, text='Java', variable=chkbox_values[1],onvalue='java',offvalue='')
check2.pack()

button = ttk.Button(root, text='click me', command=checkbox_result)
button.pack()

lable=ttk.Label(root, textvariable=lable_var)
lable.pack()

root.mainloop()
