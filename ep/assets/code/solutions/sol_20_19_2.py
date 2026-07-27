"""Solution 20.19.2 — Dividing a bill among friends

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

A broad except: would swallow unrelated bugs. Catch the specific
ZeroDivisionError that division by zero raises.

Exercise: ex_20_19_2.py
"""

bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("There must be at least one person")
