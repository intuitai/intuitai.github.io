"""Solution 6.1.3 — Storing an attribute

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

The attribute stored in __init__ is named score, but summary reads
self.grade, which was never set. Referring to self.score fixes the
AttributeError.

Exercise: ex_6_1_3.py
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.score}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
