rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ')

try:
  user_choice = int(user_choice)
  if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number. You Lose!')
  else:
    print('\nYou choose:')
    print(game_images[user_choice])


    print('\nComputer choose:')
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if user_choice == computer_choice:
      print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
      print('You Win!')
    elif user_choice == 1 and computer_choice == 0:
      print('You Win!')
    elif user_choice == 2 and computer_choice == 1:
      print('You Win!')
    else:
      print('You Lose!')
    print()
except ValueError:
  print('You typed an invalid number. You Lose!')