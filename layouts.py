# library
import tkinter as tk                    # Import base tkinter library for GUI
from tkinter import ttk                 # Import ttk module for themed widgets
from calendar import month_name         # Imported but not used (safe to remove)

# Create main window
root = tk.Tk()

# window parameters
root.title('Basic Widghts')            # Set the window title
root.geometry('800x800')               # Set the window size to 800x800 pixels
root.resizable(True, True)             # Allow resizing both horizontally and vertically

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# Create a label with text "hello" and orange background
hello_lable = ttk.Label(root, text="hello", background="Orange")

# Create a label with text "Welcome" and yellow background
welcome_lable = ttk.Label(root, text="Welcome", background="yellow")

# The following lines were used for grid layout (currently commented out)

# root.columnconfigure(0, weight=1)     # Make column 0 expandable
# root.columnconfigure(1, weight=1)     # Make column 1 expandable
# root.columnconfigure(2, weight=1)     # Make column 2 expandable
# root.rowconfigure(0, weight=1)        # Make row 0 expandable
# root.rowconfigure(1, weight=1)        # Make row 1 expandable

# Position labels using grid layout (currently not used)
# hello_lable.grid(row=1, column=1, sticky="nsew")        # Place "hello" in grid
# welcome_lable.grid(row=0, column=2, sticky="nsew")      # Place "Welcome" in grid

# Position "hello" label at x=0, y=0 (top-left corner), with size 100x100
hello_lable.place(x=0, y=0, width=100, height=100)

# Position "Welcome" label at center of window (relative 50% x and y), size 50x50
welcome_lable.place(relx=0.5, rely=0.5, width=50, height=50)

# The following are alternative packing options (currently commented out)

# hello_lable.pack(side='left', expand=True, fill="both") # Pack "hello" on left, fill and expand
# welcome_lable.pack()                                    # Pack "Welcome" normally

# Start the GUI event loop
root.mainloop()
