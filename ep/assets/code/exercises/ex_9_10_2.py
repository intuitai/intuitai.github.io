"""Exercise 9.10.2 — Weekend or weekday

Chapter 9: Control Flow — Everyday Programming

This program should print Weekend for Saturday or Sunday and Weekday
otherwise. For "Monday" it should print Weekday.

This program contains exactly one bug. Solution: sol_9_10_2.py
"""

day = "Monday"

match day:
    case "Saturday" or "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
# Expected: Weekday
