"""Solution 10.4.4 — Order of defaults

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

A parameter with a default cannot come before one without a default, so
def area(height=1, width) is a SyntaxError. Put the non-default
parameter first.

Exercise: ex_10_4_4.py
"""

def area(width, height=1):
    return width * height

print(area(width=5))  # 5
