"""Solution 5.3.2 — Passing grade

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Passed (capital P) is a different, undefined name, so printing it raises
a NameError. Print the variable passed.

Exercise: ex_5_3_2.py
"""

grade = 72
passed = grade >= 60
print(passed)   # True
