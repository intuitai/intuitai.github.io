"""Solution 20.16.1 — Converting miles to kilometers

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The function computes km but never returns it, so the call yields None.
Add a return.

Exercise: ex_20_16_1.py
"""

def miles_to_km(miles):
    km = miles * 1.60934
    return km

print("Kilometers:", miles_to_km(5))
