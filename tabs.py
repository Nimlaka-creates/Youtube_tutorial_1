# Importing necessary libraries
import tkinter as tk                          # Standard tkinter GUI library
from tkinter import ttk                       # ttk module for themed widgets
from calendar import month_name               # (Not used in this script, can be removed)

# Create main window
root = tk.Tk()
root.title('Basic Widghts')                   # Set window title
root.geometry('800x800')                      # Set window size
root.resizable(True, True)                    # Allow window to be resizable

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Function to add a name from the entry to the table
def add_name():
    table.insert('', tk.END, values=(entru_value.get(),))  # Insert value from entry as a tuple
    entru_value.get()  # (Optional/unnecessary — this line does nothing useful)

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create first tab (frame1) for input
frame1 = ttk.Frame(notebook, width=200, height=100, relief=tk.GROOVE)
frame1.pack_propagate(False)                  # Prevent frame from resizing to fit content
frame1.pack()                                 # Add frame1 to the layout (this line is optional — notebook.add handles it)

# Create a StringVar to hold entry value
entru_value = tk.StringVar()

# Create an entry box in frame1 for user input
entry = ttk.Entry(frame1, textvariable=entru_value)
entry.pack(pady=10)                           # Add vertical padding

# Create a button in frame1 to trigger add_name()
button = ttk.Button(frame1, text='Click me', command=lambda: add_name())
button.pack()

# Create second tab (frame2) for output (table display)
frame2 = ttk.Frame(notebook, width=100, height=100, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

# Create Treeview table inside frame2 with one column called "Names"
table = ttk.Treeview(frame2, columns=('Names'), show='headings')  # Hide default tree column
table.column('Names', width=200)              # Set column width
table.heading('Names', text='Names')          # Set column heading
table.pack()

# (Optional) Static data insertion example — currently commented out
# names = ["saman", "jonny"]
# for idx, value in enumerate(names):
#     table.insert('', index=idx, values=(names[idx],))

# Add frame1 to the notebook as the "INPUT" tab
notebook.add(frame1, text='INPUT')
notebook.pack()

# Add frame2 to the notebook as the "OUTPUT" tab
notebook.add(frame2, text='OUTPUT')
notebook.pack()

# Start the application loop (keeps window open)
root.mainloop()
