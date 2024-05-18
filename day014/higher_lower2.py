from game_data import data
from art import logo, vs
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Takes user's guess and follower counts and return true or false"""
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'


def get_random_account():
    return random.choice(data)


def play_game():
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        # Format acc data into printable format
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get user input on who has more followers
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        # Check if user is correct
        is_correct = check_answer(guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()