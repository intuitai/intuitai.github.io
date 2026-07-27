"""Exercise 10.5.5 — Mixing names and positions

Chapter 10: Functions — Everyday Programming

This should compute simple interest (principal times rate times years)
as 60.0.

This program contains exactly one bug. Solution: sol_10_5_5.py
"""

def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02, time=3))  # 60.0
