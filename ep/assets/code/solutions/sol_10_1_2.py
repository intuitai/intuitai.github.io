"""Solution 10.1.2 — The colon

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The def header must end with a colon. Without it Python cannot tell
where the body begins and raises a SyntaxError.

Exercise: ex_10_1_2.py
"""

def boiling_point():
    print("Water boils at 100 degrees Celsius.")

boiling_point()
