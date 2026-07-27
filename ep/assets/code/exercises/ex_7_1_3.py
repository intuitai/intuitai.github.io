"""Exercise 7.1.3 — Eggs left over

Chapter 7: Operators — Everyday Programming

A baker has 17 eggs and packs them into cartons of 6. This program
should print how many eggs are left over after filling whole cartons,
which is 5.

This program contains exactly one bug. Solution: sol_7_1_3.py
"""

total_eggs = 17
carton_size = 6
leftover = total_eggs // carton_size
print(leftover)   # expected: 5
