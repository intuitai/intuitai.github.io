"""Solution 18.2.5 — Looking up a planet

Chapter 18: Bugs — Everyday Programming

Bug type: Runtime

The key "mars" is lowercase, but the dictionary key is "Mars";
dictionary lookups are case sensitive, so this raises KeyError. Matching
the stored key returns the value.

Exercise: ex_18_2_5.py
"""

moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["Mars"])   # 2
