"""Exercise 10.11.2 — A safe default

Chapter 10: Functions — Everyday Programming

This should add a reading to a fresh list each call, printing a one-item
list each time.

This program contains exactly one bug. Solution: sol_10_11_2.py
"""

def add_reading(value, readings=[]):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
