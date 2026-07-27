"""Exercise 9.11.1 — Even check

Chapter 9: Control Flow — Everyday Programming

This function should return True when a number is even. is_even(4)
should print True.

This program contains exactly one bug. Solution: sol_9_11_1.py
"""

def is_even(number):
    number % 2 == 0

print(is_even(4))
# Expected: True
