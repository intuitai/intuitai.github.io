"""Solution 20.14.4 — Comparing two shopping lists

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

Two lists with identical contents are still distinct objects, so is is
always False here. Use == to compare contents.

Exercise: ex_20_14_4.py
"""

cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one == cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
