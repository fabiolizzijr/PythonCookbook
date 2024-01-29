# GUI with Scrolledtext widget example
#=================================
# Imports
#=================================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext # Import the module that contains ScrolledText class

# Create an instance of Tk class
win = tk.Tk()

# Add a title
win.title('GUI with Scrolledtext')

# Set up size window
win.geometry('350x300')

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
chVarDis = tk.IntVar() # The variable is int because by default is 0 or 1
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W) # sticky to W set to the left

chVarUn = tk.IntVar() # The variable is 0=unchecked or 1=checked
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W) # W stand for West

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
# Assign tkinter keywords = symbolic names to the variables
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if   radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)

# Create three Radiobuttons with one variable
# Because they are all using the same variable
# When you select one, it deselect the others!
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Using Scrolled text Control
scrol_w = 30 # scroll width
scrol_h = 3  # scroll height
# ScrolledText constructor with wrap=tk.Word, default option = tk.char
# This separate words, otherwise it break in char in middle of words between the lines
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3) # span it in the three columns

# Set focus into name Entry
name_entered.focus()

# Start GUI
win.mainloop()