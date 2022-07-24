import pandas

student_dict = {
    'student' : ["Angela", "James", "lily"],
    'score' : [56, 76, 96],
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row ) in student_data_frame.iterrows():
    print(row)