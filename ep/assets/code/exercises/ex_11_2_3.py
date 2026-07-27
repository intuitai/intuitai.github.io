"""Exercise 11.2.3 — shadowing a built-in name

Chapter 11: Scoping — Everyday Programming

This program should add up a list of grocery prices and print the total.

This program contains exactly one bug. Solution: sol_11_2_3.py
"""

prices = [2.50, 1.25, 3.00]
sum = 0

def total():
    return sum(prices)

print("Total:", total())
# Expected:
# Total: 6.75
