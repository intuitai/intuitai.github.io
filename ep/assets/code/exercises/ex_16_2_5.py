"""Exercise 16.2.5 — Percent off

Chapter 16: Handling Failures — Everyday Programming

This program reads a typed divisor, builds a fraction from it, and
should report a non-number and a zero divisor with separate messages.

This program contains exactly one bug. Solution: sol_16_2_5.py
"""

price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except Exception:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("The divisor cannot be zero.")
