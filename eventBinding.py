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
btn=ttk.Button(root,text='click me')
btn.pack()

# btn.bind('<Motion>', lambda event:print(event))
root.bind('<Enter>', lambda event:print("Enter to Window"))
root.bind('<Leave>', lambda event:print("Exit from window"))

entry=ttk.Entry(root)
entry.pack()

entry.bind('<FocusIn>', lambda event:print("Entry button Selected"))
entry.bind('<FocusOut>', lambda event:print("Entry button Not-Selected"))

root.mainloop()
