"""Exercise 20.21.2 — Summing daily sales

Chapter 20: Common Pitfalls — Everyday Programming

The program should add up every day's sales and print the total.

This program contains exactly one bug. Solution: sol_20_21_2.py
"""

sales = [120, 85, 200, 95]
total = 0
for i in range(len(sales)):
    total = total + sales
print("Total sales:", total)
