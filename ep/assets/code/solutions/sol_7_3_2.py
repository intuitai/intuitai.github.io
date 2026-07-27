"""Solution 7.3.2 — Are two distances equal?

Chapter 7: Operators — Everyday Programming

Bug type: Runtime

Inside a function call, distance_a = distance_b is read as a keyword
argument, so print raises a TypeError about an invalid keyword argument.
Comparison needs the equality operator ==.

Exercise: ex_7_3_2.py
"""

distance_a = 100
distance_b = 100
print(distance_a == distance_b)   # True
