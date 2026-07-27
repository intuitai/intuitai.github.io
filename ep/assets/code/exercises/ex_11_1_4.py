"""Exercise 11.1.4 — the helper's result must come back out

Chapter 11: Scoping — Everyday Programming

This program should compute the perimeter of a rectangle and print it at
the top level.

This program contains exactly one bug. Solution: sol_11_1_4.py
"""

def perimeter(length, width):
    edges = 2 * (length + width)

result = perimeter(5, 3)
print("Perimeter:", result)
# Expected:
# Perimeter: 16
