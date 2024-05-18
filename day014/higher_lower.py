from game_data import data
from art import logo, vs
import random
# import random
print(logo)

person1 = random.choice(data)
person2 = random.choice(data)
print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
print(vs)
print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")

print()