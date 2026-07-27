"""Exercise 10.12.1 — Mutating shares the change

Chapter 10: Functions — Everyday Programming

Appending inside the function should change the caller's list too.

This program contains exactly one bug. Solution: sol_10_12_1.py
"""

def add_one(numbers):
    numbers = numbers + [1]

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
