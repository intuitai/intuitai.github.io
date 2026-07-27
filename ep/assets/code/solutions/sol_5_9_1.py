"""Solution 5.9.1 — Looking up a name

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Keys are case-sensitive; "Name" is not in the dict, so this raises a
KeyError. Use the actual key "name".

Exercise: ex_5_9_1.py
"""

student = {"name": "Maya", "grade": 10}
print(student["name"])   # Maya
