# Creating a rock, paper and scissor GUI game example
# Using Widgets: Label, Entry, Combobox
# Using game logic from rock_paper_scissors fundamentals
#===============================================================
# Game Logic ideas:
# 1. Ask user if it wants: rock, paper, scissor or quit
# 2. Computer will generate a random number from 1 to 3
# 3. If 1 = Rock, elif 2 = Paper, else Scissor
# 4. Verify by the rules who won:
# 4.1 - If Rock Rock, Paper Paper or Scissor Scissor it is draw
# 4.2 - Rock > Scissor > Paper > Rock
# 5. print the Winner and ask for new command
#===============================================================
# Imports
#===============================================================
import tkinter as tk
from tkinter import ttk
import random

# Create a instance of TK
window = tk.Tk()

# Add title
window.title('Rock & Paper & Scissor - The Game')

# Set a fixed size -> PlayStation: 640x480
window.geometry('640x120')
# Make it non resizable
window.resizable(False, False)

# Add label for user name
username_label = ttk.Label(window, text="Enter your username:")
username_label.grid(column=0, row=0)

# Add textbox Entry for username input
username = tk.StringVar() # Assign username to special variable StringVar
username_entry = ttk.Entry(window, width=105, textvariable=username)
username_entry.grid(column=0, row=1)
username_entry.focus() # Focus so the user don't forget it!

# Add game_choice Label
game_choice_label = ttk.Label(window, text="Choose your option:")
game_choice_label.grid(column=0, row=2)

# Add game_choice Combobox with options Rock, Paper and Scissor
user_game_choice = tk.StringVar()
game_choice_combobox = ttk.Combobox(window, width=102, textvariable=user_game_choice, state='readonly')
game_choice_combobox.grid(column=0, row=3)
game_choice_combobox['values'] = ('Rock', 'Paper', 'Scissor')
game_choice_combobox.current(0) # Set default to Rock, The Rock's Rocks!

# Computer must generate randomly it's choice
# Make it a function :)
def computer_move():
    """ () -> str
    Return radomnly 'Rock', 'Paper' or 'Scissor'

    >>> computer_move()
    'Rock'
    >>> computer_move()
    'Paper'
    >>> computer_move()
    'Scissor'
    """
    computer_number = random.randint(1,3) # generates random number from 1 to 3
    if computer_number == 1:
        computer_choice = 'Rock'
    elif computer_number == 2:
        computer_choice = 'Paper'
    elif computer_number == 3:
        computer_choice = 'Scissor'
    return computer_choice

# 4. Verify by the rules who won => Making another function
def verify_victory(user_choice, computer_choice):
    """ (str) -> str
    Return victory/draw/defeat message based on user and computer choice

    >>> verify_victory('Rock', 'Paper')
    'You lose! The computer chooses Paper...'
    >>> verify_victory('Rock', 'Scissor')
    'You Win! The computer chooses Scissor...'
    >>> verify_victory('Rock', 'Rock')
    'It is a DRAW! The computer chooses Rock...'
    """
    result = ''
    if user_choice == computer_choice:
        result = "It is a DRAW! The computer chooses " + computer_choice + " too."
    elif user_choice == 'Rock' and computer_choice == 'Scissor':
        result = "You Win! The computer chooses " + computer_choice + "..."
    elif user_choice == 'Scissor' and computer_choice == 'Paper':
        result = "You Win! The computer chooses " + computer_choice + "..."
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        result = "You Win! The computer chooses " + computer_choice + "..."
    else:
        result = "You Lost! The computer chooses " + computer_choice + "..."
    return result

# Add Click_me function
def click_me():
    computer_choice = computer_move() # Get computer choice
    result = verify_victory(user_game_choice.get(), computer_choice) # Get result string
    action.configure(text="Hello " + username.get() +
                     "\n" + result)

# Add Button
action = ttk.Button(window, text="Game!", command=click_me)
action.grid(column=0, row=4)

# Start GUI
window.mainloop()