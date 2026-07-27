"""Exercise 6.4.3 — Appending to a list

Chapter 6: Objects — Everyday Programming

This program builds a list of square numbers from 1 to 5.

This program contains exactly one bug. Solution: sol_6_4_3.py
"""

squares = []
for n in range(1, 6):
    squares.append(n + n)
print(squares)   # [1, 4, 9, 16, 25]
