# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#Example Output 1
#total height = 857
#number of students = 5
#average height = 171

# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

total_students = 0
for student in student_heights:
  total_students += 1
print(f"number of students = {total_students}")


avg_height = round(total_height / total_students)
print(f"average height = {avg_height}")
