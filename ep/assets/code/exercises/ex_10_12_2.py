"""Exercise 10.12.2 — Rebinding stays local

Chapter 10: Functions — Everyday Programming

Reassigning the parameter should not change the caller's list, so this
prints the original.

This program contains exactly one bug. Solution: sol_10_12_2.py
"""

def replace(numbers):
    numbers.clear()
    numbers.extend([99, 100])

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
