# JQ 1st Fix The Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = float(input("Enter your guess: "))
        #made the guess and intiger syntax error
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
            #changed if to elif syntax error
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts = attempts + 1
        elif guess < number_to_guess:
            print("Too low! Try again.") 
            attempts = attempts + 1
            #made it add attempts when you get it wrong logic error

        else:
            print("something went wrong")
#           Added an else statement, syntax error
        continue
    print("Game Over. Thanks for playing!")
start_game()