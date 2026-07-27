"""Solution 16.4.5 — Cleanup message

Chapter 16: Handling Failures — Everyday Programming

Bug type: Syntax

The clauses are out of order: finally appears before except, which is
not allowed — except (and else) must come before finally. Reorder so
except precedes finally.

Exercise: ex_16_4_5.py
"""

try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
except ValueError:
    print("That was not a number.")
finally:
    print("Sensor reset.")
