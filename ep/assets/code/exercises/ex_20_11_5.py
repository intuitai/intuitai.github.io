"""Exercise 20.11.5 — Looping one step too far

Chapter 20: Common Pitfalls — Everyday Programming

This program should print every price in the list.

This program contains exactly one bug. Solution: sol_20_11_5.py
"""

prices = [3, 5, 9]
index = 0
while index <= len(prices):
    print(prices[index])
    index = index + 1
