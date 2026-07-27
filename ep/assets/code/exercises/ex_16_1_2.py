"""Exercise 16.1.2 — Parsing a price

Chapter 16: Handling Failures — Everyday Programming

This program should read a price like "4.99" and print double it,
recovering from bad input.

This program contains exactly one bug. Solution: sol_16_1_2.py
"""

try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except VlaueError:
    print("That was not a valid price.")
