# numbers = [1,2,3,4]
# list = [n * 2 for n in numbers]
# print(list)
#
# names = ["Pradeep", "kumar", "bharat", "Naveen", "Narendra Modi"]
# import random
#
# student_scores = {student: random.randint(1,100) for student  in names}
#
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60 }
# print(passed_students)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "scores": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key,value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.scores)