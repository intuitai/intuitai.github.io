"""Solution 20.1.4 — Missing colon after def

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

A function definition must end with : after the parameter list. Adding
the colon makes the definition valid.

Exercise: ex_20_1_4.py
"""

def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 5))  # 20
