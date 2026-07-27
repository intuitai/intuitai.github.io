"""Solution 5.8.5 — Building a set

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

{} creates an empty dictionary, not a set, so seen.add raises an
AttributeError. Use set() to create an empty set.

Exercise: ex_5_8_5.py
"""

seen = set()
seen.add("apple")
print(seen)   # {'apple'}
