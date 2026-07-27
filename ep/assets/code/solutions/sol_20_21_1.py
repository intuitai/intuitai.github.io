"""Solution 20.21.1 — Printing each planet

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

The loop indexes with i but prints planet, which was never defined,
raising NameError. Iterate over the items directly.

Exercise: ex_20_21_1.py
"""

planets = ["Mercury", "Venus", "Earth", "Mars"]
for planet in planets:
    print(planet)
