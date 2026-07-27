"""Exercise 10.4.2 — Default tax rate

Chapter 10: Functions — Everyday Programming

This function should add an 8 percent tax by default, so a 50 dollar
bill becomes 54.0.

This program contains exactly one bug. Solution: sol_10_4_2.py
"""

def with_tax(price, rate=0.08):
    return price + price * 0.8

print(with_tax(50))  # 54.0
