# Write your code below this line 👇

def prime_checker(number):
  is_prime = True

  if number < 2:
    is_prime = False
  elif number == 2 or number == 3:
    is_prime = True
  else:
    for i in range(2, number):
      if number % i == 0:
        is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input('n = ')) # Check this number
prime_checker(number=n)