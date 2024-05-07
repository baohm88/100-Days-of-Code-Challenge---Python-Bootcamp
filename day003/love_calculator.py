print("The Love Calculator is calculating your score...")
name1 = input('What is your name? ') # What is your name?
name2 = input('What is their name? ') # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = (name1 + name2).lower()

t = name.count('t')
r = name.count('r')
u = name.count('e')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')

true_score = t + r + u + e
love_score = l + o + v + e

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and.")
elif 40 <= total_score and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")