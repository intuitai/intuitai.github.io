"""Exercise 20.16.1 — Converting miles to kilometers

Chapter 20: Common Pitfalls — Everyday Programming

This program should print the distance in kilometers for 5 miles.

This program contains exactly one bug. Solution: sol_20_16_1.py
"""

def miles_to_km(miles):
    km = miles * 1.60934

print("Kilometers:", miles_to_km(5))
