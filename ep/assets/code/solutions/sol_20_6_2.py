"""Solution 20.6.2 — Adding a number to a string label

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Mixing str and int with + raises TypeError. Convert liters to a string
before concatenating.

Exercise: ex_20_6_2.py
"""

liters = 2
print("Drink " + str(liters) + " liters")
