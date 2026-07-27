"""Solution 18.4.4 — Sale price

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Printing sale_price shows it equals the discount amount, not the
discounted price, so the subtraction yields the wrong savings. The
savings are simply price * discount_rate.

Exercise: ex_18_4_4.py
"""

def savings(price, discount_rate):
    return price * discount_rate

print(savings(120, 0.30))   # 36.0
