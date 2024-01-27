# GUI with textbox widget example
#================================
# Imports
#================================
import tkinter as tk
from tkinter import ttk

# Create an instance of Tk class
win = tk.Tk()

# Add title
win.title('GUI with textbox widget')

# Create a label
a_label = ttk.Label(win, text="Enter a name:")
a_label.grid(column=0, row=0)

# Create a function for the button
def click_me():
    action_bt.configure(text="Hello " + name.get())

# Create one-line textbox widget which is called => Entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Create action_bt Button
action_bt = ttk.Button(win, text="Click me!", command=click_me)
action_bt.grid(column=1, row=1)

# Start GUI
win.mainloop()