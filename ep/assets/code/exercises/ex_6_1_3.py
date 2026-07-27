"""Exercise 6.1.3 — Storing an attribute

Chapter 6: Objects — Everyday Programming

This class records a student's name and quiz score, then prints a
summary.

This program contains exactly one bug. Solution: sol_6_1_3.py
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.grade}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
