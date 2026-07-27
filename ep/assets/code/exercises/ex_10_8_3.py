"""Exercise 10.8.3 — Reading the docstring

Chapter 10: Functions — Everyday Programming

This program should print the docstring of the function.

This program contains exactly one bug. Solution: sol_10_8_3.py
"""

def half(number):
    """Return half of a number."""
    return number / 2

print(half.__docs__)
