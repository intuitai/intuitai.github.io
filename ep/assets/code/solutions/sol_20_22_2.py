"""Solution 20.22.2 — Totaling a receipt

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

sum = 0 shadows the built-in sum, so sum(prices) tries to call an
integer and raises TypeError. Use a different variable name.

Exercise: ex_20_22_2.py
"""

running_total = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
