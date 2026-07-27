"""Exercise 20.16.3 — Doubling a recipe

Chapter 20: Common Pitfalls — Everyday Programming

This program should return the doubled amount of flour.

This program contains exactly one bug. Solution: sol_20_16_3.py
"""

def double_amount(cups):
    doubled = cups * 2

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
