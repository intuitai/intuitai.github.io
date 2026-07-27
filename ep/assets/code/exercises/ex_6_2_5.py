"""Exercise 6.2.5 — Reading a class constant

Chapter 6: Objects — Everyday Programming

The class stores a fixed sales-tax rate shared by all carts; each cart
has its own subtotal. The total should add the tax.

This program contains exactly one bug. Solution: sol_6_2_5.py
"""

class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal / self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
