"""Exercise 20.17.3 — Counting visitors

Chapter 20: Common Pitfalls — Everyday Programming

The program should increase the visitor count by one each time someone
enters.

This program contains exactly one bug. Solution: sol_20_17_3.py
"""

visitors = 0

def enter():
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
