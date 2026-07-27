"""Solution 20.12.4 — Listing class names

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

subjects is a tuple, so append raises AttributeError. Use square
brackets for a list.

Exercise: ex_20_12_4.py
"""

subjects = ["Math", "Science"]
subjects.append("History")
print(subjects)
