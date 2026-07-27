"""Solution 20.22.1 — Counting items in a basket

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Assigning len = [4, 8, 15] shadows the built-in len, so len(fruit) tries
to call a list and raises TypeError. Rename the variable.

Exercise: ex_20_22_1.py
"""

basket = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
