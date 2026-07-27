"""Solution 11.2.4 — which value gets printed

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

The local tax_rate is set to 0.08, but the formula hard-codes 0.05, so
the local shadow is never used and the answer is 105.0. Use the local
tax_rate in the calculation.

Exercise: ex_11_2_4.py
"""

tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * tax_rate

print("With tax:", quote(100))
