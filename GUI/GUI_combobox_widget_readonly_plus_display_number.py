# GUI combobox widget with readonly property and display number button
#=====================================================================
# Imports
#=====================================================================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add title
win.title('GUI Combobox widget readonly display number')

# Add label for the entry textbox
entry_label = ttk.Label(win, text="Enter your name:")
entry_label.grid(column=0, row=0)

# Add textbox Entry
name = tk.StringVar() # Assign name to special tk variable
name_entered = ttk.Entry(win, textvariable=name)
name_entered.grid(column=0, row=1)

# Define function click_me
def click_me():
    action.configure(text="Hello " + name.get() + ' ' +
                     number_chosen.get())

# Add button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1)

# Add combobox label
combobox_label = ttk.Label(win, text="Choose a number:")
combobox_label.grid(column=1, row=0)

# Add combobox
number = tk.StringVar() # Assign number to special type StringVar of tk
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly') # Make readonly
number_chosen['values'] = (1, 2, 4, 16, 42, 100) # Tuple with default values
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Start GUI
win.mainloop()