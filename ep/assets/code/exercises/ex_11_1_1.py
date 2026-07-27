"""Exercise 11.1.1 — reading a global from a function

Chapter 11: Scoping — Everyday Programming

This program should print the speed limit twice: once from inside
report() and once from the top level.

This program contains exactly one bug. Solution: sol_11_1_1.py
"""

speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit)
# Expected:
# Inside: 100
# Outside: 100
