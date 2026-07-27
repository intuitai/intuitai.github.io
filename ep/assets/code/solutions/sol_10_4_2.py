"""Solution 10.4.2 — Default tax rate

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The body multiplies by the literal 0.8 instead of the rate parameter,
charging 80 percent. Use rate so the default 0.08 applies.

Exercise: ex_10_4_2.py
"""

def with_tax(price, rate=0.08):
    return price + price * rate

print(with_tax(50))  # 54.0
