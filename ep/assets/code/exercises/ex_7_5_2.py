"""Exercise 7.5.2 — Odd number not in list

Chapter 7: Operators — Everyday Programming

This program should check that 7 is not among the listed even numbers
and print True.

This program contains exactly one bug. Solution: sol_7_5_2.py
"""

even_numbers = [2, 4, 6, 8]
number = 7
result = number in not even_numbers
print(result)   # expected: True
