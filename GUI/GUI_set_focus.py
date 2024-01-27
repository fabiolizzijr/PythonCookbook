# GUI set focus example
#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk

# Create instance of Tk Class
win = tk.Tk()

# Set title
win.title('GUI with focus')

# Create label
my_label = ttk.Label(win, text="Enter your name:")
my_label.grid(column=0, row=0)

# Adding textbox Entry
name = tk.StringVar()
name_entered = ttk.Entry(win, textvariable=name)
name_entered.grid(column=0, row=1)

# Create function click_me()
def click_me():
    action_bt.configure(text="Hello " + name.get())
    """ () -> Shows Hello + name typed in textbox Entry
    """
# Adding a Button
action_bt = ttk.Button(win, text="Click me!", command=click_me)
action_bt.grid(column=1, row=1)
action_bt.configure(state='disabled') # Disable the Button Widget

name_entered.focus() # Place the cursor into name Entry
#======================================================
# Start GUI
#======================================================
win.mainloop()