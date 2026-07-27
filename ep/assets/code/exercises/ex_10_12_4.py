"""Exercise 10.12.4 — Mutate in place

Chapter 10: Functions — Everyday Programming

This should add a grade to the shared list in place, so the caller sees
three items.

This program contains exactly one bug. Solution: sol_10_12_4.py
"""

def record_grade(grades, grade):
    grades = grades + [grade]

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
