"""Exercise 20.26.5 — Noting one ingredient

Chapter 20: Common Pitfalls — Everyday Programming

Each call should produce a fresh list containing only the ingredient
given.

This program contains exactly one bug. Solution: sol_20_26_5.py
"""

def note_ingredient(name, items=[]):
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
