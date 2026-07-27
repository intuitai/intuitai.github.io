"""Solution 20.16.3 — Doubling a recipe

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

doubled is computed but not returned, so flour becomes None. Add return
doubled.

Exercise: ex_20_16_3.py
"""

def double_amount(cups):
    doubled = cups * 2
    return doubled

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
