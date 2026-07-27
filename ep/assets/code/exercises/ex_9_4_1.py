"""Exercise 9.4.1 — Sum of a list

Chapter 9: Control Flow — Everyday Programming

This program should add up the prices in a cart and print the total, 60.

This program contains exactly one bug. Solution: sol_9_4_1.py
"""

prices = [10, 20, 30]
total = 0

for price in prices:
    total = price

print("Total:", total)
# Expected: Total: 60
