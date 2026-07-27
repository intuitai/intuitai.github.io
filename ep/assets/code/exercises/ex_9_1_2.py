"""Exercise 9.1.2 — Temperature category

Chapter 9: Control Flow — Everyday Programming

This program should classify a temperature in Celsius. With 36.5 it
should print only Heat warning.

This program contains exactly one bug. Solution: sol_9_1_2.py
"""

temp_c = 36.5

if temp_c > 35:
print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
