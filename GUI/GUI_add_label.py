# GUI with an label example
# ttk modules has advanced widgets to make GUI look GREAT!
# it stands for themed tk - Make things look cool baby!
# ===========================
# Imports
# ===========================
import tkinter as tk
from tkinter import ttk # import ttk module from tkinter package

# Create an instance of Tk class
win = tk.Tk()

# Create a title in GUI
win.title('GUI with label example')

# Adding a label
# ttk.Label() constructor
# ttk.Label(window_instance, text)
# ttk.Label(win, text="Hello").grid() - calls grid layout manager
ttk.Label(win, text="A Label").grid(column=0, row=0)

# Start GUI
win.mainloop()