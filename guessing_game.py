import random

# Game setup
print("Welcome to the Guessing game")
number_of_guesses = 3 # USer has 3 guesses before loses the game
user_won = False

# Computer generates a random number from 1 to 10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
    # User guesses the number
    print("You have " + str(number_of_guesses) + " guesses...")
    user_guess = int(input("Guess my number from 1 to 10: "))

    # Computer tells the user if the guess is too high or low
    if user_guess == correct_answer:
        print("Good guess")
        print("You are correct!")
        user_won = True
        break
    elif user_guess < correct_answer:
        print("Sorry! You guessed to low")
    else:
        print("Sorry! You guessed to high")

    number_of_guesses -= 1 # Decrease 1 guesses

if user_won == True:
    print("YOU WIN!")
else:
    print("YOU LOST!")