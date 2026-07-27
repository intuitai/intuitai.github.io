"""Solution 18.2.2 — Final price with tax

Chapter 18: Bugs — Everyday Programming

Bug type: Runtime

The expression references tax, but the variable defined above is
tax_rate, so Python raises a NameError. Using the correct name computes
the taxed price.

Exercise: ex_18_2_2.py
"""

price = 50.0
tax_rate = 0.08
final_price = price + (price * tax_rate)
print(final_price)   # 54.0
