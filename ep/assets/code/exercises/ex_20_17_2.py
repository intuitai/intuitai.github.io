"""Exercise 20.17.2 — Keeping a running balance

Chapter 20: Common Pitfalls — Everyday Programming

This program should subtract a withdrawal from the account balance.

This program contains exactly one bug. Solution: sol_20_17_2.py
"""

balance = 500

def withdraw(amount):
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
