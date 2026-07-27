"""Solution 5.5.2 — Default color

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The function changes color but never returns it, so it returns None. Add
a return color statement.

Exercise: ex_5_5_2.py
"""

def choose_color(color):
    if color is None:
        color = "blue"
    return color

print(choose_color(None))   # blue
