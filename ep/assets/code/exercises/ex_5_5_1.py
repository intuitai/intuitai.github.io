"""Exercise 5.5.1 — No reading yet

Chapter 5: Data Structures — Everyday Programming

A sensor has no reading. The program should print True because the
reading is None.

This program contains exactly one bug. Solution: sol_5_5_1.py
"""

reading = None
no_data = reading == "None"
print(no_data)   # True
