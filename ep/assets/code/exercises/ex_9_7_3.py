"""Exercise 9.7.3 — Search for a name

Chapter 9: Control Flow — Everyday Programming

This program should stop as soon as it finds "Ana" and print Found.

This program contains exactly one bug. Solution: sol_9_7_3.py
"""

names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        brake
