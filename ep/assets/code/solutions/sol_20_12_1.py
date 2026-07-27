"""Solution 20.12.1 — Building a shopping list

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Parentheses create a tuple, which has no append method, so the call
raises AttributeError. Use square brackets to make a list.

Exercise: ex_20_12_1.py
"""

groceries = ["milk", "bread", "eggs"]
groceries.append("butter")
print(groceries)
