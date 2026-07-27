"""Exercise 16.4.2 — Releasing the scale

Chapter 16: Handling Failures — Everyday Programming

This program weighs an item and must always print that the scale is
released, even when input is bad.

This program contains exactly one bug. Solution: sol_16_4_2.py
"""

try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
else:
    print("Scale released.")
