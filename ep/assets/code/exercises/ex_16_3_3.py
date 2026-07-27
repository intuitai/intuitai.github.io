"""Exercise 16.3.3 — Doubling a recipe

Chapter 16: Handling Failures — Everyday Programming

This program reads a cup amount and, when valid, prints the doubled
amount using else.

This program contains exactly one bug. Solution: sol_16_3_3.py
"""

try:
    cups = float(input("How many cups? "))
    doubled = cups * 2
    print("You need", doubled, "cups.")
except ValueError:
    print("That was not a number.")
else:
    print("Measurement accepted.")
