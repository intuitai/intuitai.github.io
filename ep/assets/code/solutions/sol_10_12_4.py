"""Solution 10.12.4 — Mutate in place

Chapter 10: Functions — Everyday Programming

Bug type: Logical

grades = grades + [grade] rebinds the local name to a new list, so the
caller's list is unchanged. Use append to mutate the shared list in
place.

Exercise: ex_10_12_4.py
"""

def record_grade(grades, grade):
    grades.append(grade)

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
