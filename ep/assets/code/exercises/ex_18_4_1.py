"""Exercise 18.4.1 — Total grocery cost

Chapter 18: Bugs — Everyday Programming

This program should print the total cost of three grocery items, but the
answer is wrong. Trace it with print and find the single wrong line.

This program contains exactly one bug. Solution: sol_18_4_1.py
"""

def total_cost(apples, bread, milk):
    subtotal = apples + bread - milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # expected: 7.5
