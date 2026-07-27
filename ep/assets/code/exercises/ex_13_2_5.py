"""Exercise 13.2.5 — Kelvin conversion formula

Chapter 13: Modules — Everyday Programming

This two-file program should convert 0 degrees Celsius to Kelvin
(273.15).

This program contains exactly one bug. Solution: sol_13_2_5.py
"""

# file: conversions.py
def c_to_k(celsius):
    return celsius - 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
