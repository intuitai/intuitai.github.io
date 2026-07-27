"""Solution 9.4.1 — Sum of a list

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

total = price overwrites the running sum each pass instead of adding to
it, leaving only the last price. Use total += price to accumulate.

Exercise: ex_9_4_1.py
"""

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print("Total:", total)
