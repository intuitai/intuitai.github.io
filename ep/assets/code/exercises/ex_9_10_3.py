"""Exercise 9.10.3 — Locating a point

Chapter 9: Control Flow — Everyday Programming

This program should describe a point. For (0, 5) it should print On the
y-axis at 5.

This program contains exactly one bug. Solution: sol_9_10_3.py
"""

point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, y):
        print("Somewhere else:", x, y)
    case (0, y):
        print("On the y-axis at", y)
# Expected: On the y-axis at 5
