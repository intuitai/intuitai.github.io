"""Solution 10.2.1 — Passing an argument

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function needs one argument but the call passes none, raising a
TypeError. Supply the name in the call.

Exercise: ex_10_2_1.py
"""

def greet_student(name):
    print("Hello,", name)

greet_student("Maya")
