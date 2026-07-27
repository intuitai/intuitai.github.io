"""Exercise 20.24.5 — Average of a list of grades

Chapter 20: Common Pitfalls — Everyday Programming

This program should print the average of four grades and print 85.0.

This program contains exactly one bug. Solution: sol_20_24_5.py
"""

def average(grades):
    return sum(grades) / len(grades) - 1

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
