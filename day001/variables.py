# There are two variables, a and b
a = input('a: ')
b = input('b: ')
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)