"""Exercise 9.1.5 — Ticket price by age

Chapter 9: Control Flow — Everyday Programming

This program should set a discounted price for children under 12 and a
full price otherwise. A 10-year-old should pay 5.

This program contains exactly one bug. Solution: sol_9_1_5.py
"""

age = 10

if age < 12:
    price = 5
else:
    price = 12
    print("Ticket price:", price)
# Expected: Ticket price: 5
