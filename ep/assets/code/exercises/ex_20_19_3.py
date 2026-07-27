"""Exercise 20.19.3 — Looking up a price

Chapter 20: Common Pitfalls — Everyday Programming

This program should read a price from a dictionary and warn only when
the item is missing.

This program contains exactly one bug. Solution: sol_20_19_3.py
"""

prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except:
    print("That item is not on the price list")
