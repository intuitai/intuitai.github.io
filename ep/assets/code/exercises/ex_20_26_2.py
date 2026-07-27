"""Exercise 20.26.2 — Building a grocery list

Chapter 20: Common Pitfalls — Everyday Programming

Each call should begin with a fresh, empty cart and add one item.

This program contains exactly one bug. Solution: sol_20_26_2.py
"""

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
