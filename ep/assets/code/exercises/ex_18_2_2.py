"""Exercise 18.2.2 — Final price with tax

Chapter 18: Bugs — Everyday Programming

This program should print a $50 item's price after 8% sales tax.

This program contains exactly one bug. Solution: sol_18_2_2.py
"""

price = 50.0
tax_rate = 0.08
final_price = price + (price * tax)
print(final_price)   # expected: 54.0
