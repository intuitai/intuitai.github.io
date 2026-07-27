"""Exercise 9.11.2 — Describe a number

Chapter 9: Control Flow — Everyday Programming

This function should return "positive", "negative", or "zero".
describe(-3) should print negative.

This program contains exactly one bug. Solution: sol_9_11_2.py
"""

def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        "negative"
    else:
        return "zero"

print(describe(-3))
# Expected: negative
