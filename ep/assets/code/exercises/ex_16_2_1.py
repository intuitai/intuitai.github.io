"""Exercise 16.2.1 — Splitting a bill

Chapter 16: Handling Failures — Everyday Programming

This program divides a restaurant bill among friends and should report
when there are zero friends.

This program contains exactly one bug. Solution: sol_16_2_1.py
"""

bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ValueError:
    print("There must be at least one person.")
