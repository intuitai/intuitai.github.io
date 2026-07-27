"""Exercise 20.17.1 — Tallying rainfall

Chapter 20: Common Pitfalls — Everyday Programming

The program should add today's rainfall to the running total and print
it.

This program contains exactly one bug. Solution: sol_20_17_1.py
"""

total_rain = 0.0

def add_rain(today):
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
