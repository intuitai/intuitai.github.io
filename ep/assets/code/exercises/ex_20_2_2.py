"""Exercise 20.2.2 — Inconsistent indentation in a loop

Chapter 20: Common Pitfalls — Everyday Programming

This program should add up the rainfall for three days.

This program contains exactly one bug. Solution: sol_20_2_2.py
"""

rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
      print(total)  # 35
