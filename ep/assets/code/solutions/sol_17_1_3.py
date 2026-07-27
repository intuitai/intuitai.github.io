"""Solution 17.1.3 — Average of three grades

Chapter 17: Testing — Everyday Programming

Bug type: Logical

Operator precedence divides only c by 3 before adding, instead of
dividing the whole sum. Parentheses around the sum fix the formula so
the average is computed correctly.

Exercise: ex_17_1_3.py
"""

def average(a, b, c):
    return (a + b + c) / 3

assert average(80, 90, 100) == 90
print("passed")
