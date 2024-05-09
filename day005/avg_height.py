# Input a Python list of student heights
student_heights = input('Student heights: ').split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
num_students = len(student_heights)
sum_height = 0
for i in range(0, num_students):
  sum_height += student_heights[i]

avg_height = round(sum_height / num_students)
print('total height = ' + str(sum_height))
print('number of students = ' + str(num_students))
print('average height = ' + str(avg_height))
