"""Exercise 16.3.1 — Confirming a conversion

Chapter 16: Handling Failures — Everyday Programming

This program converts a string to a number and, only when that succeeds,
prints a success line.

This program contains exactly one bug. Solution: sol_16_3_1.py
"""

text = "42"
try:
    number = int(text)
    print("Conversion worked:", number)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
