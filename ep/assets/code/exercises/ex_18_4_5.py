"""Exercise 18.4.5 — Speed from distance and time

Chapter 18: Bugs — Everyday Programming

This program should print speed in kilometres per hour, but the answer
is wrong. Trace it with print and find the single wrong line.

This program contains exactly one bug. Solution: sol_18_4_5.py
"""

def speed(distance_km, time_hours):
    result = time_hours / distance_km
    return result

print(speed(150, 3))   # expected: 50.0
