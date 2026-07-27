"""Solution 6.1.4 — Calling a method

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

The method is called on the class, Account.add_interest(0.05), so 0.05
is bound to self and no rate is supplied, raising a TypeError. Calling
it on the instance, savings.add_interest(0.05), passes savings as self
and 0.05 as rate.

Exercise: ex_6_1_4.py
"""

class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
savings.add_interest(0.05)
print(savings.balance)   # 1050.0
