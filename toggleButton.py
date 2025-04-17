# library
import tkinter as tk                    # Import base tkinter library for GUI
from tkinter import ttk                 # Import ttk module for themed widgets
from calendar import month_name         # Imported but not used (safe to remove)

# Create main window
root = tk.Tk()

# window parameters
root.title('Basic Widghts')            # Set the window title
root.geometry('400x400')               # Set the window size to 400x400 pixels
root.resizable(True, True)             # Allow window to be resizable in both directions

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Create a BooleanVar to track the state of the bulb (True = ON, False = OFF)
bulb_state = tk.BooleanVar(value=False)  # Initial state is OFF

# Function to toggle the state of the bulb
def change_state():
    if bulb_state.get():                # If bulb is ON
        bulb_state.set(False)           # Set it to OFF
        bulb.configure(text='OFF')      # Update label to show 'OFF'
    else:                               # If bulb is OFF
        bulb_state.set(True)            # Set it to ON
        bulb.configure(text='ON')       # Update label to show 'ON'
    print(bulb_state.get())             # Print current state in the console (for debugging)

# Create a button labeled "Switch" that calls change_state() when clicked
switch = ttk.Button(root, text="Switch", command=change_state)
switch.pack(side='bottom', pady=20)     # Place it at the bottom with vertical padding

# Create a label to represent the bulb's state (initially OFF)
bulb = ttk.Label(text='OFF')
bulb.place(relx=0.5, rely=0.4)          # Place the label at center horizontally and 40% from the top

# Start the GUI event loop
root.mainloop()
