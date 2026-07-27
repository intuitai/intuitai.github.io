"""Exercise 7.4.4 — Safe to swim

Chapter 7: Operators — Everyday Programming

It is safe to swim if a lifeguard is on duty and the water is calm. This
program should print True.

This program contains exactly one bug. Solution: sol_7_4_4.py
"""

lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm:
print(safe_to_swim)   # expected: True
