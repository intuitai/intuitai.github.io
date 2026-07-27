"""Solution 20.11.3 — Showing the third prize

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

The list has only two items (indexes 0 and 1), so prizes[2] raises
IndexError. To print a third prize, the list must contain one.

Exercise: ex_20_11_3.py
"""

prizes = ["gold", "silver", "bronze"]
print(prizes[2])
