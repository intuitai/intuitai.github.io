"""Solution 20.26.5 — Noting one ingredient

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The mutable default items=[] is reused on every call, so ingredients
accumulate. Default to None and make a fresh list.

Exercise: ex_20_26_5.py
"""

def note_ingredient(name, items=None):
    if items is None:
        items = []
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
