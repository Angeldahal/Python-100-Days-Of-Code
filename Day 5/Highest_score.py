student_scores = input("Input the scores of the students:\n").split()


Highest_score = 0
for High_score in student_scores:
    if(int(Highest_score)<int(High_score)):
        Highest_score = High_score

print(f"The Highest Score in the class is: {Highest_score}")