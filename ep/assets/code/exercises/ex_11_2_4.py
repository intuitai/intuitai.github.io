"""Exercise 11.2.4 — which value gets printed

Chapter 11: Scoping — Everyday Programming

The global tax_rate is 0.05. Inside quote() a local tax_rate of 0.08
should be used to compute the price with tax. The program should print
108.0.

This program contains exactly one bug. Solution: sol_11_2_4.py
"""

tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * 0.05

print("With tax:", quote(100))
# Expected:
# With tax: 108.0
