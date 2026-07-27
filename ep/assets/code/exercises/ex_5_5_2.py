"""Exercise 5.5.2 — Default color

Chapter 5: Data Structures — Everyday Programming

The function should return a default color when none is given. Calling
it with nothing should print "blue".

This program contains exactly one bug. Solution: sol_5_5_2.py
"""

def choose_color(color):
    if color is None:
        color = "blue"

print(choose_color(None))   # blue
