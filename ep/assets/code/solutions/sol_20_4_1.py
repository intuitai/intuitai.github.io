"""Solution 20.4.1 — Printing before assigning

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

students is used on the first line but assigned on the second, raising
NameError. Assign before using.

Exercise: ex_20_4_1.py
"""

students = 30
print(students)
