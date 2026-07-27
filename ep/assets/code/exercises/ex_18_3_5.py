"""Exercise 18.3.5 — Fahrenheit to Celsius

Chapter 18: Bugs — Everyday Programming

This program should convert 212 degrees Fahrenheit to Celsius.

This program contains exactly one bug. Solution: sol_18_3_5.py
"""

def f_to_c(f):
    return (f - 32) * 9 / 5

print(f_to_c(212))   # expected: 100.0
