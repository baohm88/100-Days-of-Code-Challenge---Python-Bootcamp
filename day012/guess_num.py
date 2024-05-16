#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

computer_choice = random.randint(0, 100)
game_over = False
user_attempt_count = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Shhh, the correct answer is {computer_choice}")
mode = input("Choose a level. Type 'easy' or 'hard': ").lower()
if mode == 'easy':
    user_attempt_count = 10
else:
    user_attempt_count = 5

print(f"Remaining attemps: {user_attempt_count}")
print(f"You have {user_attempt_count} attempts remaining to guess the number.")

while not game_over:    
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_choice:
        print(f"You got it. The answer was {computer_choice}")
        game_over = True
    elif user_guess > computer_choice:
        user_attempt_count -= 1
        print(f"Too high.\nGuess again.\nYou have {user_attempt_count} attempts remaining to guess the number.")
    else:
        user_attempt_count -= 1
        print(f"Too low.\nGuess again.\nYou have {user_attempt_count} attempts remaining to guess the number.")

    if user_attempt_count == 0:
        print(f"You've run out of guesses, you lose.")
