"""Exercise 10.6.4 — Order of the tuple

Chapter 10: Functions — Everyday Programming

This should report width then height of a 8 by 3 rectangle, printing
"width 8 height 3".

This program contains exactly one bug. Solution: sol_10_6_4.py
"""

def dimensions():
    return 3, 8

width, height = dimensions()
print("width", width, "height", height)
