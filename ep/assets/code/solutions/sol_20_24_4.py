"""Solution 20.24.4 — Celsius to Fahrenheit

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The formula adds 32, but the code subtracts it. Change - 32 to + 32.

Exercise: ex_20_24_4.py
"""

def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
