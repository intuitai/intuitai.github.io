"""Exercise 7.1.5 — Total cost with tax

Chapter 7: Operators — Everyday Programming

An item costs $20 and tax is 10%. This program should print the total
cost including tax, which is 22.0.

This program contains exactly one bug. Solution: sol_7_1_5.py
"""

price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total   # expected: 22.0
