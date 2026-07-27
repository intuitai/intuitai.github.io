"""Solution 9.9.3 — Doing nothing where logic was needed

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The loop body is left as pass, so nothing is added and the total stays
0. The real work—accumulating the prices—must replace the placeholder.

Exercise: ex_9_9_3.py
"""

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(total)
