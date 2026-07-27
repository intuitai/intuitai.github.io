"""Exercise 10.12.3 — Integers are immutable

Chapter 10: Functions — Everyday Programming

Changing the parameter inside the function should not affect the
caller's number, which stays 5.

This program contains exactly one bug. Solution: sol_10_12_3.py
"""

def add_ten(value):
    global score
    score = value + 10

score = 5
add_ten(score)
print(score)   # expected: 5
