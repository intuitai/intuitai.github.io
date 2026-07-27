"""Exercise 13.2.3 — The main guard

Chapter 13: Modules — Everyday Programming

This module should print a sample conversion only when run directly, but
it should still work when imported.

This program contains exactly one bug. Solution: sol_13_2_3.py
"""

# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ = "__main__":
    print(c_to_f(100))   # 212.0
