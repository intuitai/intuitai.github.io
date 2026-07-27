"""Exercise 11.2.5 — parameter shadows the global

Chapter 11: Scoping — Everyday Programming

The global gravity is 9.8. The function takes its own gravity as a
parameter so a caller can test the Moon's 1.6. The program should print
the weight on the Moon.

This program contains exactly one bug. Solution: sol_11_2_5.py
"""

gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 9.8))
# Expected:
# Moon weight: 16.0
