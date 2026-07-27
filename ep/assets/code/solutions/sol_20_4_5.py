"""Solution 20.4.5 — Using a price before defining it

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

price is multiplied before it is assigned, raising NameError. Define
price before the calculation.

Exercise: ex_20_4_5.py
"""

quantity = 3
price = 2
print(quantity * price)
