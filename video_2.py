#basic widgets
#library
import tkinter as tk
from tkinter import ttk 
root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('300x200')
root.resizable(False,True)

#function to get entrys from entry field to lable
def button_click_function():
    # entry_field_value=entry.get()
    #lable.configure(text=entry_field_value)
    lable.configure(text=entry.get())
    button2.configure(state='disabled')
    
    
#entry field initialization 
entry = ttk.Entry(root)
entry.pack()

#button initialization
button2 = tk.Button(root, text="click me!!",command=button_click_function)
button2.pack()

#lable initialization
lable = ttk.Label(root)
lable.pack()
lable.configure( text='Hello')

root.mainloop()
