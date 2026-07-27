"""Exercise 9.4.5 — Largest measurement

Chapter 9: Control Flow — Everyday Programming

This program should find the largest of several distances and print it,
45.

This program contains exactly one bug. Solution: sol_9_4_5.py
"""

distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance < largest:
        largest = distance

print(largest)
# Expected: 45
