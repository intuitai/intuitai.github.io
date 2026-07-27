"""Exercise 18.4.4 — Sale price

Chapter 18: Bugs — Everyday Programming

This program should print the savings on a $120 item at 30% off, but the
answer is wrong. Trace it with print and find the single wrong line.

This program contains exactly one bug. Solution: sol_18_4_4.py
"""

def savings(price, discount_rate):
    sale_price = price * discount_rate
    return price - sale_price

print(savings(120, 0.30))   # expected: 36.0
