"""Exercise 5.2.2 — Splitting a bill

Chapter 5: Data Structures — Everyday Programming

A 50-dollar bill is split between 4 people. The program should print
12.5.

This program contains exactly one bug. Solution: sol_5_2_2.py
"""

bill = 50
people = 4

each = bill // people
print(each)   # 12.5
