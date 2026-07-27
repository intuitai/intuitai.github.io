"""Exercise 10.4.3 — Overriding the default

Chapter 10: Functions — Everyday Programming

This program should print 200 by overriding the default step count.

This program contains exactly one bug. Solution: sol_10_4_3.py
"""

def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 200))  # 200
