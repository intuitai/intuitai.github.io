"""Exercise 16.4.5 — Cleanup message

Chapter 16: Handling Failures — Everyday Programming

This program reads a distance and must always print a cleanup line at
the very end, no matter what happens.

This program contains exactly one bug. Solution: sol_16_4_5.py
"""

try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
finally:
    print("Sensor reset.")
except ValueError:
    print("That was not a number.")
