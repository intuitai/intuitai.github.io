"""Exercise 5.7.2 — A fixed pair

Chapter 5: Data Structures — Everyday Programming

This program should change the width to 1280 and print (1280, 1080).

This program contains exactly one bug. Solution: sol_5_7_2.py
"""

size = (1920, 1080)
size[0] = 1280
print(size)   # expected: (1280, 1080)
