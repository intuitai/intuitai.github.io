"""Solution 20.21.5 — Listing the ingredients

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

item becomes the index 0, 1, 2 instead of the ingredient name. Iterate
over the list itself.

Exercise: ex_20_21_5.py
"""

ingredients = ["flour", "sugar", "butter"]
for item in ingredients:
    print(item)
