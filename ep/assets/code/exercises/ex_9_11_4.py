"""Exercise 9.11.4 — Total with tax

Chapter 9: Control Flow — Everyday Programming

This function should return the price plus 10% tax. with_tax(100) should
print 110.0.

This program contains exactly one bug. Solution: sol_9_11_4.py
"""

def with_tax(price):
    tax = price * 0.10
    return price
    total = price + tax

print(with_tax(100))
# Expected: 110.0
