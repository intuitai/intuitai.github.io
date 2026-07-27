"""Exercise 20.16.2 — Averaging three test grades

Chapter 20: Common Pitfalls — Everyday Programming

The program should print the average of three grades.

This program contains exactly one bug. Solution: sol_20_16_2.py
"""

def average(a, b, c):
    total = a + b + c
    average_value = total / 3

print("Average:", average(80, 90, 100))
