"""Solution 18.1.1 — Rectangle perimeter

Chapter 18: Bugs — Everyday Programming

Bug type: Syntax

The def header is missing the colon that must end every function
definition line, so Python cannot parse the file. Adding the colon lets
the function be defined and called.

Exercise: ex_18_1_1.py
"""

def perimeter(length, width):
    return 2 * (length + width)

print(perimeter(8, 5))   # 26
