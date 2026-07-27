"""Solution 5.6.4 — Changing a value

Chapter 5: Data Structures — Everyday Programming

Bug type: Syntax

Item assignment uses square brackets, not parentheses; prices(1) = 5.0
is not valid Python. Use prices[1] = 5.0.

Exercise: ex_5_6_4.py
"""

prices = [2.0, 3.0, 4.0]
prices[1] = 5.0
print(prices)   # [2.0, 5.0, 4.0]
