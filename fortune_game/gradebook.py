last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
my_subjects = ["physics", "calculus", "poetry", "history"]
my_grades = [98, 97, 85, 88]
this_semester_gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

new_subject_grade = ["computer science", 100]
this_semester_gradebook.append(new_subject_grade)
new_grade = ("visual arts", 93)
this_semester_gradebook.append(new_grade)
this_semester_gradebook[-1] = list(this_semester_gradebook[-1])

# Update the grade for the last subject added
this_semester_gradebook[-1][1] += 5

# Remove and replace the grade for poetry with "Pass"
this_semester_gradebook.remove(['poetry', 85])
this_semester_gradebook.append(["poetry", "Pass"])
full_gradebook = last_semester_gradebook + this_semester_gradebook
print(full_gradebook)
