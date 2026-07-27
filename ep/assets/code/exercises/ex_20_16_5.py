"""Exercise 20.16.5 — Tax on a purchase

Chapter 20: Common Pitfalls — Everyday Programming

This program should return the tax owed on a $200 purchase at 8 percent.

This program contains exactly one bug. Solution: sol_20_16_5.py
"""

def tax_owed(price, rate):
    tax = price * rate / 100

print("Tax:", tax_owed(200, 8))
