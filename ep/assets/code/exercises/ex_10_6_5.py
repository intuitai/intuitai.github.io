"""Exercise 10.6.5 — Returning both values

Chapter 10: Functions — Everyday Programming

This program should return and print both the sum and the product of 4
and 5.

This program contains exactly one bug. Solution: sol_10_6_5.py
"""

def sum_and_product(a, b):
    return a + b
    return a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
