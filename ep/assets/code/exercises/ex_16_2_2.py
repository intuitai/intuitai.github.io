"""Exercise 16.2.2 — Adding a measurement

Chapter 16: Handling Failures — Everyday Programming

This program adds a typed measurement to a running total and warns if
the text is not a number.

This program contains exactly one bug. Solution: sol_16_2_2.py
"""

total = 100
new_value = "twelve"
try:
    total = total + new_value
except ZeroDivisionError:
    print("That measurement was not a number.")
print("Total is", total)
