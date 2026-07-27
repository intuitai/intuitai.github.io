"""Exercise 20.19.2 — Dividing a bill among friends

Chapter 20: Common Pitfalls — Everyday Programming

The program should split a bill and report only when the number of
people is zero.

This program contains exactly one bug. Solution: sol_20_19_2.py
"""

bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except:
    print("There must be at least one person")
