"""Exercise 20.24.1 — Average speed of a trip

Chapter 20: Common Pitfalls — Everyday Programming

This program should compute average speed (distance over time) for a 150
km trip in 3 hours and print 50.0.

This program contains exactly one bug. Solution: sol_20_24_1.py
"""

def average_speed(distance, time):
    return time / distance

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
