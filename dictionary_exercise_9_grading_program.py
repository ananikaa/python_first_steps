student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def score_to_grade(score):
    if score in range(91, 101):
        return 'Outstanding'
    elif score in range(81, 91):
        return 'Exceeds Expectations'
    elif score in range(71, 81):
        return 'Acceptable'
    else:
        return 'Fail'

# print(score_to_grade(96))

student_grades = {}

for key, value in student_scores.items():
    student_grades[key] = score_to_grade(value)

# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
# The final version of the student_grades dictionary will be checked.
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"