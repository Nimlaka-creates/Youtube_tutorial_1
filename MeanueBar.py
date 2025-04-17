# Import necessary libraries
import tkinter as tk                # Standard GUI module
from tkinter import ttk             # Themed tkinter widgets
from calendar import month_name     # (Not used in this script, can be removed)

# Create the main application window
root = tk.Tk()
root.title('Basic Widghts')         # Set window title
root.geometry('800x800')            # Set window size (width x height)
root.resizable(True, True)          # Allow window to be resizable both horizontally and vertically

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Create the main menu bar for the window
menu = tk.Menu(root)

# Create a StringVar to hold the state of a menu checkbutton (used later)
light_result = tk.StringVar(value='OFF')  # Initial state is OFF

# Create the "File" dropdown menu
file_menu = tk.Menu(menu, tearoff=False)  # `tearoff=False` disables the dashed line at the top
file_menu.add_command(label="New file", command=lambda: print("New file"))   # Adds "New file" option with print action
file_menu.add_command(label="Open file", command=lambda: print("Open File")) # Adds "Open file" option with print action

# Add the File dropdown menu to the menu bar
menu.add_cascade(label='File', menu=file_menu)

# Create the "Results" dropdown menu
result_menu = tk.Menu(menu, tearoff=False)
result_menu.add_command(label="display")  # Just a label option (no command assigned)

# Adds a checkbutton item (toggle) to the Results menu
result_menu.add_checkbutton(
    label="restart",                      # Label of the checkbutton
    variable=light_result,                # Links to the StringVar so it can store state
    onvalue="On",                         # Value when checked
    offvalue="Off",                       # Value when unchecked
    command=lambda: print(light_result.get())  # Prints the current state when toggled
)

# Add the Results dropdown menu to the menu bar
menu.add_cascade(label='Results', menu=result_menu)

# Attach the whole menu to the root window
root.configure(menu=menu)

# Run the application (starts the GUI loop)
root.mainloop()
