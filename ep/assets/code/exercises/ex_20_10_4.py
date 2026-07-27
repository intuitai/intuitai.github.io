"""Exercise 20.10.4 — Adding a fourth runner's time

Chapter 20: Common Pitfalls — Everyday Programming

This program should store a fourth lap time at the next position.

This program contains exactly one bug. Solution: sol_20_10_4.py
"""

lap_times = [45, 47, 44]
lap_times[len(lap_times)] = 46
print(lap_times)
