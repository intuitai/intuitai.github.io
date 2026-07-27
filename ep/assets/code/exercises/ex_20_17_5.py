"""Exercise 20.17.5 — Building a points streak

Chapter 20: Common Pitfalls — Everyday Programming

The program should multiply the current streak by 2 each round.

This program contains exactly one bug. Solution: sol_20_17_5.py
"""

streak = 1

def double_streak():
    streak = streak * 2

double_streak()
print("Streak:", streak)
