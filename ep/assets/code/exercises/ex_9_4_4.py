"""Exercise 9.4.4 — Average of readings

Chapter 9: Control Flow — Everyday Programming

This program should print the average of three temperature readings,
30.0.

This program contains exactly one bug. Solution: sol_9_4_4.py
"""

readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(reading)
print(average)
# Expected: 30.0
