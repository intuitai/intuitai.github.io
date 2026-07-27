"""Solution 20.4.2 — Using a sum before it exists

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

total is printed before it is computed, causing NameError. Move the
assignment above the print.

Exercise: ex_20_4_2.py
"""

first = 70
second = 85
total = first + second
print(total)
