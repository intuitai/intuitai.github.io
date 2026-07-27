"""Exercise 20.24.4 — Celsius to Fahrenheit

Chapter 20: Common Pitfalls — Everyday Programming

The program should convert 100 degrees Celsius to Fahrenheit and print
212.0.

This program contains exactly one bug. Solution: sol_20_24_4.py
"""

def to_fahrenheit(celsius):
    return celsius * 9 / 5 - 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
