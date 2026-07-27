"""Solution 10.8.4 — Closing the quotes

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The triple-quoted docstring is never closed, so Python reads the rest of
the file as part of the string and raises a SyntaxError. Close the
docstring.

Exercise: ex_10_8_4.py
"""

def square_perimeter(side):
    """Return the perimeter of a square."""
    return side * 4

print(square_perimeter(3))  # 12
