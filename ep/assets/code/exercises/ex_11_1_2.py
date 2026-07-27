"""Exercise 11.1.2 — a local name stays local

Chapter 11: Scoping — Everyday Programming

A scientist measures a temperature inside a helper function. The program
should print the reading from inside the function only.

This program contains exactly one bug. Solution: sol_11_1_2.py
"""

def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
print("Confirmed:", temperature_c)
# Expected:
# Reading: 21.5
