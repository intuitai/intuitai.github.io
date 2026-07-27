"""Exercise 17.1.2 — Celsius to Fahrenheit check

Chapter 17: Testing — Everyday Programming

The function converts Celsius to Fahrenheit, and the assert should
confirm that 100 °C is 212 °F.

This program contains exactly one bug. Solution: sol_17_1_2.py
"""

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 211
print("passed")
