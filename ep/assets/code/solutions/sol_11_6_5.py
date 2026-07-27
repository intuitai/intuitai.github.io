"""Solution 11.6.5 — updating an instance attribute

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

deposit assigns to a local balance, which vanishes when the method
returns; the object's self.balance is never updated, so it stays 50.
Assign to self.balance.

Exercise: ex_11_6_5.py
"""

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
