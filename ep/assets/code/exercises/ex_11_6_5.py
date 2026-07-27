"""Exercise 11.6.5 — updating an instance attribute

Chapter 11: Scoping — Everyday Programming

This program saves money into an account and should print the balance,
70, after one deposit.

This program contains exactly one bug. Solution: sol_11_6_5.py
"""

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
# Expected:
# Balance: 70
