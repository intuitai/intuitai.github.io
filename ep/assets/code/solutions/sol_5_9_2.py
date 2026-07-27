"""Solution 5.9.2 — Updating a grade

Chapter 5: Data Structures — Everyday Programming

Bug type: Syntax

Dictionary assignment uses square brackets, not parentheses;
student("grade") = 11 is invalid. Use student["grade"] = 11.

Exercise: ex_5_9_2.py
"""

student = {"name": "Maya", "grade": 10}
student["grade"] = 11
print(student["grade"])   # 11
