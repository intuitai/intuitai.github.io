"""Solution 11.5.2 — running total in an enclosing scope

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

A deposit should add to the total, but the code subtracts, so the
balance goes negative. Use addition.

Exercise: ex_11_5_2.py
"""

def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total + amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
