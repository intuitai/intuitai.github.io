"""Solution 6.2.5 — Reading a class constant

Chapter 6: Objects — Everyday Programming

Bug type: Logical

Sales tax is added by *multiplying* the subtotal by the rate, not
dividing by it. The corrected line uses self.subtotal + self.subtotal *
self.tax_rate, giving 54.0.

Exercise: ex_6_2_5.py
"""

class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal * self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
