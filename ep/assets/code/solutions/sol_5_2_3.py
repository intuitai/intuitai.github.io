"""Solution 5.2.3 — Rounding a price

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

round(price) with no second argument rounds to a whole number (3). Pass
2 to round to two decimal places.

Exercise: ex_5_2_3.py
"""

price = 3.14159
rounded = round(price, 2)
print(rounded)   # 3.14
