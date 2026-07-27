"""Solution 20.11.4 — Last item by length

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

len(students) is 3, one past the last index, so students[3] raises
IndexError. The last index is len(students) - 1.

Exercise: ex_20_11_4.py
"""

students = ["Mia", "Noah", "Liam"]
print(students[len(students) - 1])
