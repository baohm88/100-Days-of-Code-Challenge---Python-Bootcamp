import random

names = input('Names: ').split(", ")
length = len(names)
rand_index = random.randint(0, length -1)
print(f"{names[rand_index]} is gonna buy the meal today!")