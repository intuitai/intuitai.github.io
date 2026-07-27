"""Exercise 16.4.1 — Closing a report

Chapter 16: Handling Failures — Everyday Programming

This program divides two numbers and should always print a closing line,
whether or not the division fails.

This program contains exactly one bug. Solution: sol_16_4_1.py
"""

try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
    print("Done with the calculation.")
