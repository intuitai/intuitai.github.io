"""Solution 20.13.5 — Correcting a unit label

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

unit[0] = "K" tries to mutate an immutable string, raising TypeError.
Make a new string instead.

Exercise: ex_20_13_5.py
"""

unit = "km"
unit = "K" + unit[1:]
print(unit)
