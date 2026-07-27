"""Solution 20.17.2 — Keeping a running balance

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

The function assigns to balance, so Python treats it as local and the
read raises UnboundLocalError. Add global balance.

Exercise: ex_20_17_2.py
"""

balance = 500

def withdraw(amount):
    global balance
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
