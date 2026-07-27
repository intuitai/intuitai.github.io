"""Solution 20.13.1 — Capitalizing a name

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Strings are immutable, so name[0] = "S" raises TypeError. Build a new
string instead.

Exercise: ex_20_13_1.py
"""

name = "sam"
name = "S" + name[1:]
print(name)
