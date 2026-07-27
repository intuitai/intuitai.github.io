"""Solution 9.10.2 — Weekend or weekday

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

In a case pattern, alternatives are joined with |, not the keyword or.
Using | fixes the pattern.

Exercise: ex_9_10_2.py
"""

day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
