"""Solution 11.1.5 — global list, read inside the function

Chapter 11: Scoping — Everyday Programming

Bug type: Syntax

The def line is missing its colon, so the file will not parse. Add the
colon after the parentheses.

Exercise: ex_11_1_5.py
"""

scores = [80, 90, 100]

def average():
    return sum(scores) / len(scores)

print("Average:", average())
