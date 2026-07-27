"""Exercise 10.10.3 — Lambda with map

Chapter 10: Functions — Everyday Programming

This should double every number in the list, giving [2, 4, 6].

This program contains exactly one bug. Solution: sol_10_10_3.py
"""

numbers = [1, 2, 3]
doubled = list(map(lambda n: n + 2, numbers))
print(doubled)  # [2, 4, 6]
