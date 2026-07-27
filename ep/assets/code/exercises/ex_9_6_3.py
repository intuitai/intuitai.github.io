"""Exercise 9.6.3 — Doubling savings

Chapter 9: Control Flow — Everyday Programming

Starting at $1, this should double the balance until it reaches at least
$8, printing each balance.

This program contains exactly one bug. Solution: sol_9_6_3.py
"""

balance = 1

while balance < 8:
    print(balance)
    balance = balance + 2

# Expected: 1 2 4 (one per line)
