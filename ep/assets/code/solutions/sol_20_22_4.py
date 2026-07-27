"""Solution 20.22.4 — Labeling a measurement

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

str = "kilograms" shadows the built-in str, so str(weight) tries to call
a string and raises TypeError. Rename the variable.

Exercise: ex_20_22_4.py
"""

unit = "kilograms"
weight = 70
print(str(weight) + " " + unit)
