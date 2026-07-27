"""Exercise 13.2.1 — Importing your own helper

Chapter 13: Modules — Everyday Programming

This two-file program should convert 100 degrees Celsius to Fahrenheit
(212.0).

This program contains exactly one bug. Solution: sol_13_2_1.py
"""

# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_k

print(c_to_f(100))   # 212.0
