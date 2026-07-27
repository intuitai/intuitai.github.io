"""Exercise 11.6.2 — reading an instance attribute

Chapter 11: Scoping — Everyday Programming

This program stores a student's score and should print it back as 95.

This program contains exactly one bug. Solution: sol_11_6_2.py
"""

class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return score

learner = Student(95)
print("Score:", learner.get_score())
# Expected:
# Score: 95
