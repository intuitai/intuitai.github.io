"""Exercise 11.5.2 — running total in an enclosing scope

Chapter 11: Scoping — Everyday Programming

This program adds amounts into an enclosing total using nonlocal, and
should print 30 after two deposits.

This program contains exactly one bug. Solution: sol_11_5_2.py
"""

def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total - amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
# Expected:
# Balance: 30
