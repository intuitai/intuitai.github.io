"""Solution 18.3.4 — Discounted price

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Multiplying by the discount rate gives the amount taken off, not the
price paid, so the result is 20 instead of 60. The customer pays the
remaining fraction, 1 - discount_rate.

Exercise: ex_18_3_4.py
"""

price = 80.0
discount_rate = 0.25
final_price = price * (1 - discount_rate)
print(final_price)   # 60.0
