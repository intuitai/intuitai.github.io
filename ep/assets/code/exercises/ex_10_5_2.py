"""Exercise 10.5.2 — Order independence

Chapter 10: Functions — Everyday Programming

Keyword arguments let you reorder; this should print the speed as
distance over time, 20.0.

This program contains exactly one bug. Solution: sol_10_5_2.py
"""

def speed(distance, time):
    return distance / time

print(speed(time=100, distance=5))  # 20.0
