"""Solution 20.26.2 — Building a grocery list

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The mutable default cart=[] is shared between calls, so items pile up.
Use None and create a new list inside the function.

Exercise: ex_20_26_2.py
"""

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
