"""Exercise 6.1.2 — Using self

Chapter 6: Objects — Everyday Programming

This class converts a Celsius reading to Fahrenheit.

This program contains exactly one bug. Solution: sol_6_1_2.py
"""

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
