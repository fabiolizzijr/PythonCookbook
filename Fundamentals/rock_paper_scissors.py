# Rock paper and scissors game example
# First make it work on CLI
# Then create new with GUI knowledge
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
# Import random module
import random

# 1. Ask user if it wants: rock, paper, scissor or quit
user_command = ''
while user_command != 'quit':
    print("*------------Welcome to ROCK-PAPER-SCISSOR GAME------------*")
    print("Choose a valid option: Rock, Paper, Scissor or quit")
    user_command = input("Your choice is: ").lower()
    # If user's want to quit, do nothing more after
    if user_command.lower() == 'quit':
        break
    # 2. Computer will generate a random number from 1 to 3
    computer_number = random.randint(1,3)

    # 3. If 1 = Rock, elif 2 = Paper, else Scissor
    if computer_number == 1:
        computer_choice = 'rock'
    elif computer_number == 2:
        computer_choice = 'paper'
    elif computer_number == 3:
        computer_choice = 'scissor'

    # 4. Verify by the rules who won:
    result = ''
    # 4.1 - If Rock Rock, Paper Paper or Scissor Scissor it is draw
    if user_command.lower() == 'rock' and computer_choice == 'rock':
        result = 'DRAW! Try Again!!!'
    elif user_command.lower() == 'paper' and computer_choice == 'paper':
        result = 'DRAW! Try Again!!!'
    elif user_command.lower() == 'scissor' and computer_choice == 'scissor':
        result = 'DRAW! Try Again!!!'
    # 4.2 - Rock > Scissor > Paper > Rock
    elif user_command.lower() == 'rock' and computer_choice == 'scissor':
        result = 'Victory!'
    elif user_command.lower() == 'scissor' and computer_choice == 'paper':
        result = 'Victory!'
    elif user_command.lower() == 'paper' and computer_choice == 'rock':
        result = 'Victory'
    else:
        result = 'Defeat! What have you done ?!'

    # 5. print the Winner and ask for new command
    print(f"You choose: {user_command}\nThe computer: {computer_choice}\n")
    print(result)