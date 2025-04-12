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
canvas=tk.Canvas(root,bg='white')
canvas.pack()

# ((x,y,breth,height)fill color)
# canvas.create_rectangle((10,50,100,200),fill='grey')
# canvas.create_oval((110,160,200,250),fill='red')
# canvas.create_polygon((255,20,260,155,340,100),fill='green')
# canvas.create_line((100,100,0,0),fill='red',width=5)

brush_width=1

def draw(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='green')

def start_drawing(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='green')
    canvas.bind('<B1-Motion>',draw)
       
canvas.bind('<Button-1>', start_drawing)
# canvas.bind('<Motion>',draw)

root.mainloop()

