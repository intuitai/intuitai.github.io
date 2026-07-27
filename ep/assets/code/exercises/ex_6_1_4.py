"""Exercise 6.1.4 — Calling a method

Chapter 6: Objects — Everyday Programming

This class models a savings account and adds interest to the balance.

This program contains exactly one bug. Solution: sol_6_1_4.py
"""

class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
Account.add_interest(0.05)
print(savings.balance)   # 1050.0
