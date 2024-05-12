# Def fn without parameter

# def greet():
#   print('Hello')
#   print('How do you do?')
#   print("Isn't the weather nice today?")

# greet()

# FN with 1 para
# def greet_with_name(name):
#   print(f'Hello, {name}')
#   print('How do you do ' + name + "?")
#   print("Isn't the weather nice today?")

# greet_with_name('Bao Ha')

def greet_with(name, location):
  print(f"Hello, {name}!")
  print(f"What's it like in {location}?")

greet_with(name='Bao',location= 'Hanoi')
greet_with(location= 'Hanoi', name='Bao')

