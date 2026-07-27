"""Exercise 20.14.4 — Comparing two shopping lists

Chapter 20: Common Pitfalls — Everyday Programming

The program should report that two grocery lists hold the same items.

This program contains exactly one bug. Solution: sol_20_14_4.py
"""

cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one is cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
