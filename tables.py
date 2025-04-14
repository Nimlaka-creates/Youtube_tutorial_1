#library
import tkinter as tk
from tkinter import ttk 
from calendar import month_name

root = tk.Tk()

#window parameters
root.title('Basic Widghts')
root.geometry('800x800')
root.resizable(True,True)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////

table = ttk.Treeview(root, columns=('name','age','email'), show='headings')
table.heading('name', text='name')
table.heading('age', text='age')
table.heading('email', text='email')

name=['kamal','saman','nimal','sumana']
age =[34,23,55,62]

for idx, value in enumerate(name):
    table.insert('',idx, values=(name[idx], age[idx], f'{name[idx]}@gmail.com'))
    
    
# table.insert('',0, values=('kamal',20,'kamal@gmail.com'))
# table.insert('',1, values=('saman',20,'saman@gmail.com'))
def selected_item(event):
    print(table.item(table.selection()))
    lable.configure(text=table.item(table.selection()))
    
table.bind('<<TreeviewSelect>>', lambda event:selected_item(event))

lable=ttk.Label(root)
lable.pack()

table.pack()

root.mainloop()
