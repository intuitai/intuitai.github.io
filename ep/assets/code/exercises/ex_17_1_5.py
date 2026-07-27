"""Exercise 17.1.5 — Total cost with tax

Chapter 17: Testing — Everyday Programming

The function should add 10% tax to a price, and the assert should pass
for a $20 item costing $22.

This program contains exactly one bug. Solution: sol_17_1_5.py
"""

def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 20
print("passed")
