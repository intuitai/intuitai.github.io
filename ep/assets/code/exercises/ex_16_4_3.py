"""Exercise 16.4.3 — Logging an attempt

Chapter 16: Handling Failures — Everyday Programming

This program parses a count and must always log that an attempt was
made, regardless of success.

This program contains exactly one bug. Solution: sol_16_4_3.py
"""

try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally
    print("Attempt logged.")
