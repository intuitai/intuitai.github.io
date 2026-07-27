"""Solution 11.6.2 — reading an instance attribute

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

get_score returns plain score, which is not a local or global name, so
Python raises NameError. Read the attribute through self.score.

Exercise: ex_11_6_2.py
"""

class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

learner = Student(95)
print("Score:", learner.get_score())
