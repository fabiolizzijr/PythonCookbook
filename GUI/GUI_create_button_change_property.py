# GUI with a buttons that changes
# a property of another widget
# ===============================
# Imports
# ===============================
import tkinter as tk
from tkinter import ttk

# Create a instance of Tk class
win = tk.Tk()

# Add a title
win.title('GUI with button')

# Create a label widget that will be modified
a_label = ttk.Label(win, text="A new Label")
a_label.grid(column=0, row=0)

# Button Click Event Function
def click_me():
    # Update text of the Button
    action.configure(text="** I have been Clicked! **")
    # Update the label, changing the foreground(font color) and text properties
    a_label.configure(foreground='red')
    a_label.configure(text="A Red Label")

# Adding a button
# NOTICE: DO NOT use parentheses, it's event-drive!!!
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=0)

# Start GUI
win.mainloop()