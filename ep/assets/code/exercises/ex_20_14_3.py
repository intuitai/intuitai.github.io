"""Exercise 20.14.3 — Confirming a recipe title

Chapter 20: Common Pitfalls — Everyday Programming

A recipe title is built from its words and should match the saved title.

This program contains exactly one bug. Solution: sol_20_14_3.py
"""

saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title is saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
