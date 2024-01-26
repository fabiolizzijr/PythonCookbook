# GUI not resizable example
# =========================
# Imports
# =========================
import tkinter as tk

# Create a instance of class Tk
window = tk.Tk()

# Set a title
window.title('GUI not resizable example')

# Set specific width x height
window.geometry('350x400')

# Make it not resizable by passing values 0, 0 or False, False
window.resizable(False,False)

# Enable resize of x-dimension
# window.resizable(True, False)

# Start GUI
window.mainloop()