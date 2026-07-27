"""Exercise 11.4.1 — declaring global

Chapter 11: Scoping — Everyday Programming

This program should use global so visitors is increased by the function,
and print 1.

This program contains exactly one bug. Solution: sol_11_4_1.py
"""

visitors = 0

def arrive():
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
# Expected:
# Visitors: 1
