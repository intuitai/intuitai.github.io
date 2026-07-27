"""Exercise 10.3.4 — Return what was asked

Chapter 10: Functions — Everyday Programming

This function should return the larger of two numbers; here it should
return 9.

This program contains exactly one bug. Solution: sol_10_3_4.py
"""

def larger(a, b):
    if a > b:
        return a
    else:
        return a

print(larger(4, 9))  # 9
