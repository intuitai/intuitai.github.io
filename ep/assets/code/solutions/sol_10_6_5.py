"""Solution 10.6.5 — Returning both values

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The first return exits the function, so it returns a single integer and
tuple unpacking raises a TypeError. Return both values in one tuple.

Exercise: ex_10_6_5.py
"""

def sum_and_product(a, b):
    return a + b, a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
