"""Solution 20.4.3 — Using a result before computing it

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

area is referenced before it is assigned, raising NameError. Compute
area first, then print it.

Exercise: ex_20_4_3.py
"""

radius = 3
area = 3.14159 * radius * radius
print(area)
