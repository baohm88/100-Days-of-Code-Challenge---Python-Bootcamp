line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input('Where do you want to put the treasure? ') # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
col = position[0].lower()
line = int(position[1])
if col == 'a':
  col = 0
elif col == 'b':
  col = 1
else:
  col = 2

if line == 1:
  line1[col] = 'X'
elif line == 2:
  line2[col] = 'X'
else:
  line3[col] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")