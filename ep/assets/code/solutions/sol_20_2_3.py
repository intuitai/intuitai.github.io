"""Solution 20.2.3 — Function body not indented

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The return statement must be indented inside the function. Indenting it
four spaces makes the definition valid.

Exercise: ex_20_2_3.py
"""

def square_perimeter(side):
    return 4 * side

print(square_perimeter(6))  # 24
