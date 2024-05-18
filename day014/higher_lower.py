from game_data import data
from art import logo, vs
import random

game_over = False
user_score = 0
while not game_over:
    # import random
    print(logo)
    # Generate random account
    person1 = random.choice(data)
    person2 = random.choice(data)

    # Format acc data into printable format
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)
    print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")

    # Get user input on who has more followers
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # Check if user is correct
    if user_choice == 'A':
        # Get follower count of each account
        # Use if statement to check if user is correct
        if person1['follower_count'] > person2['follower_count']:
            user_score += 1
            # Give use feedback on their guess
            print(f"You'r right!. Current score: {user_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            game_over = True
    else:
        if person1['follower_count'] < person2['follower_count']:
            user_score += 1
            print(f"You'r right!. Current score: {user_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            game_over = True
    

