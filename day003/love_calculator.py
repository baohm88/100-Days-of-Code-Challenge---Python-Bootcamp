print("The Love Calculator is calculating your score...")
name1 = input('What is your name? ') # What is your name?
name2 = input('What is their name? ') # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1 + name2
name = name.lower()


t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true_score = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love_score = l + o + v + e

score = int(str(true_score) + str(love_score))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")