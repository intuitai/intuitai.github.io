"""Exercise 11.5.1 — nonlocal counter

Chapter 11: Scoping — Everyday Programming

This program builds a counter with a nested function. nonlocal should
let increment() change the enclosing count, so the two calls print 1
then 2.

This program contains exactly one bug. Solution: sol_11_5_1.py
"""

def make_counter():
    count = 0

    def increment():
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
# Expected:
# 1
# 2
