"""Solution 20.22.5 — Finding the largest reading

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

max = 9999 shadows the built-in max, so max(readings) tries to call an
integer and raises TypeError. Use a different name.

Exercise: ex_20_22_5.py
"""

ceiling = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
