PLACEHOLDER = "[name]"

with open("E:/PradeepKumar B C/Udemy/PythonProjects/PythonProject/Mail+Merge+Project+Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("E:/PradeepKumar B C/Udemy/PythonProjects/PythonProject/Mail+Merge+Project+Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        new_letter = names_file.replace(PLACEHOLDER, name)
        print(new_letter)