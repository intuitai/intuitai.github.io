"""Exercise 10.10.4 — Lambda with filter

Chapter 10: Functions — Everyday Programming

This should keep only the even numbers, giving [2, 4].

This program contains exactly one bug. Solution: sol_10_10_4.py
"""

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 1, numbers))
print(evens)  # [2, 4]
