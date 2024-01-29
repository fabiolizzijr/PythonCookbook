# GUI with combobox widget example
#=================================
# Imports
#=================================
import tkinter as tk
from tkinter import ttk

# Create an instance of Tk class
win = tk.Tk()

# Add a title
win.title('GUI with combobox')

# Set up size window
win.geometry('250x300')

# Add Label
label = ttk.Label(win, text="Enter name:")
label.grid(column=0, row=0)

# Add textbox Entry
name = tk.StringVar() # need to create StringVar in tk
name_entered = ttk.Entry(win, textvariable=name)
name_entered.grid(column=0, row=1)

# Define click_me() function, we are NOT using OOP YET!
def click_me():
    action.configure(text="Hello " + name.get())

# Add a Button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1) # <= Change column to 2

# Add label and a combobox
ttk.Label(win, text="Choose a number:").grid(column=1, row=0) # Add label to combobox
number = tk.StringVar() # Assign a variable to tkinter special StringVar type
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 4, 100) # Creates a tuple with default values
number_chosen.grid(column=1, row=1)
number_chosen.current(0) # First value of the tuple as default value

# Add 3 Checkbox
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# Set focus into name Entry
name_entered.focus()

# Start GUI
win.mainloop()