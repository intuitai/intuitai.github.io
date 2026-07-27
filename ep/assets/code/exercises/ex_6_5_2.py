"""Exercise 6.5.2 — Making a shallow copy

Chapter 6: Objects — Everyday Programming

This should make an independent copy of a flat list of prices.

This program contains exactly one bug. Solution: sol_6_5_2.py
"""

prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
