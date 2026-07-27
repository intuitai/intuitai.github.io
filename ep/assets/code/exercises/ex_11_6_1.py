"""Exercise 11.6.1 — self attribute vs local

Chapter 11: Scoping — Everyday Programming

This program creates a thermometer and should print its stored
temperature, 22.

This program contains exactly one bug. Solution: sol_11_6_1.py
"""

class Thermometer:
    def __init__(self, temperature):
        temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
# Expected:
# Temp: 22
