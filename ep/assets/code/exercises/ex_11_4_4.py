"""Exercise 11.4.4 — accumulate into a global

Chapter 11: Scoping — Everyday Programming

This program should use global to add each deposit into the module-level
savings, ending at 60.

This program contains exactly one bug. Solution: sol_11_4_4.py
"""

savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", saving)
# Expected:
# Savings: 60
