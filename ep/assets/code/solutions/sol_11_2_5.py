"""Solution 11.2.5 — parameter shadows the global

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

The parameter gravity shadows the global, which is exactly what lets a
caller test the Moon, but the call passes 9.8 (Earth) instead of 1.6.
Pass the Moon's value as the argument.

Exercise: ex_11_2_5.py
"""

gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 1.6))
