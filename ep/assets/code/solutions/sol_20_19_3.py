"""Solution 20.19.3 — Looking up a price

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The bare except: hides all errors. A missing dictionary key raises
KeyError, so catch exactly that.

Exercise: ex_20_19_3.py
"""

prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except KeyError:
    print("That item is not on the price list")
