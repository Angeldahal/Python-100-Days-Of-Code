student_heights = input("Input a list of student heights:").split()
sum_height = 0
n = 0
for height in student_heights:
    sum_height=int(height)+sum_height
    n =n+1
average_height = sum_height/n
print(f"The Average height of the students is {average_height}")