"""Exercise 8.1.1 — Doubling a recipe

Chapter 8: Input and Output — Everyday Programming

This program asks how many cookies a recipe makes, then prints double
that amount.

This program contains exactly one bug. Solution: sol_8_1_1.py
"""

# Assume the user types: 12
cookies = input("How many cookies does the recipe make? ")
print(f"Doubled, that is {cookies * 2} cookies.")
