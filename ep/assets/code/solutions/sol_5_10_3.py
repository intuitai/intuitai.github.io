"""Solution 5.10.3 — Checking a type

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The price is a float, but the check compares against int, so it reports
False. Compare against float.

Exercise: ex_5_10_3.py
"""

price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == float)   # True
