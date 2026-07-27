"""Solution 11.2.3 — shadowing a built-in name

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The global sum = 0 shadows the built-in sum function, so sum(prices)
tries to call an integer and raises TypeError. Remove the shadowing
variable so the built-in is used.

Exercise: ex_11_2_3.py
"""

prices = [2.50, 1.25, 3.00]

def total():
    return sum(prices)

print("Total:", total())
