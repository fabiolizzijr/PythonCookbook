# GUI Add padding example
#===================================================
# Imports
#===================================================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create Instance of Tk class, a window
win = tk.Tk()

# Set title
win.title("GUI add padding to LabelFrame")

# Add Label
label_entry = ttk.Label(win, text="Enter name:")
label_entry.grid(column=0, row=0)

# Add textbox Entry
name = tk.StringVar() # Create a StringVar for name
name_entered = ttk.Entry(win, textvariable=name)
name_entered.grid(column=0, row=1)

# Define click_me() function
def click_me():
    """
    click_me()
    -> Display Hello + name.get + number.get
    """
    action.configure(text="Hello " + name.get() +
                     " your number: "+ number.get())

# Add a Button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1)

# Add label and a combobox
number_label = ttk.Label(win, text="Choose a number:")
number_label.grid(column=1, row=0)

# Add combobox
number = tk.StringVar() # Create a variable number of type StringVar
number_chosen = ttk.Combobox(win, textvariable=number)
number_chosen.grid(column=1, row=1)
number_chosen['values'] = (1, 2, 4, 16, 42, 100) # create a tuple for the special key 'values'
number_chosen.current(0) # set default to first value of 'values' tuple

# Add 3 Checkbox using loop
chkVar = [tk.IntVar(), tk.IntVar(), tk.IntVar()] # Creating list of 3 different variables
chkText = ["Disabled", "UnChecked", "Enabled"] # Create list of 3 different texts
curCheck = [tk.Checkbutton(), tk.Checkbutton, tk.Checkbutton] # Create list of 3 buttons
# curCheck[0] = "Disabled", curCheck[1] = "UnChecked", curCheck[2] = "Enabled"
for col in range(3):
    curCheck[col] = tk.Checkbutton(win, text=chkText[col], variable=chkVar[col])
    curCheck[col].grid(column=col, row=4, sticky=tk.W)

curCheck[0].configure(state='disabled')
curCheck[1].deselect()
curCheck[2].select()

# Reassign Radiobutton Globals variable to a list
colors = ['Blue', 'Gold', 'Red']

# Radiobutton Callback with new list variable
def radCall():
    radSel = radVar.get()
    if   radSel == 0: win.configure(background=colors[radSel])
    elif radSel == 1: win.configure(background=colors[radSel])
    elif radSel == 2: win.configure(background=colors[radSel])

# Create three Radiobuttons with one variable!
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
# This so Radiobuttons won't be select in starting, only when selected
radVar.set(99)

# Now we will create all three Radiobuttons with one loop
for col in range(len(colors)):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Using Scrolled text Control
scrol_w = 30 # scroll width
scrol_h = 3  # scroll height

# ScrolledText constructor with wrap=tk.Word, default option = tk.char
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)

 # span it in the three columns
scr.grid(column=0, columnspan=3)

# Create a container to hold the labels
buttons_frame = ttk.Labelframe(win, text="Labels in a frame ")
buttons_frame.grid(column=0, row=7, padx=20, pady=40)        # adding padding
# buttons_frame.grid(column=1, row=7)      # now in column1

# Place Labels in the container element with a loop :)
# To create Layer labels Horizontal alignment --Label1--Label2--Label3
# for col in range(3):
#     ttk.Label(buttons_frame, text="Label"+str(col+1)).grid(column=col, row=7, sticky=tk.W)

# Creating different alignment, Layer labels vertically--Label1--
#                                                      --Label2--
for row in range(3):                                 # --Label3--
    ttk.Label(buttons_frame, text="Label"+str(row+1)).grid(column=0, row=row, sticky=tk.W)

# Set focus into name Entry
name_entered.focus()

# Start GUI
win.mainloop()