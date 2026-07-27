"""Exercise 10.5.3 — Spelling the keyword

Chapter 10: Functions — Everyday Programming

This program should print a labeled temperature using a keyword
argument.

This program contains exactly one bug. Solution: sol_10_5_3.py
"""

def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temp=30)
