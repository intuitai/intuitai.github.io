"""Solution 16.3.5 — Tax on a purchase

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The tax formula uses addition (amount + 0.08) instead of multiplication,
so it adds eight cents rather than computing 8 percent of the amount.
Use amount * 0.08.

Exercise: ex_16_3_5.py
"""

try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount * 0.08
    print("Tax is", tax)
