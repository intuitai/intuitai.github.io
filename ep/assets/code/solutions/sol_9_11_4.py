"""Solution 9.11.4 — Total with tax

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The function returns price before computing the total, so the line after
return never runs. Returning price + tax gives the taxed total.

Exercise: ex_9_11_4.py
"""

def with_tax(price):
    tax = price * 0.10
    total = price + tax
    return total

print(with_tax(100))
