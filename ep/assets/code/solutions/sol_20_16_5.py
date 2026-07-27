"""Solution 20.16.5 — Tax on a purchase

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The tax is computed into tax but never returned, so the result is None.
Add a return.

Exercise: ex_20_16_5.py
"""

def tax_owed(price, rate):
    tax = price * rate / 100
    return tax

print("Tax:", tax_owed(200, 8))
