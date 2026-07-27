"""Exercise 7.4.1 — Eligible to vote

Chapter 7: Operators — Everyday Programming

A person may vote only if they are at least 18 *and* a citizen. This
adult is not a citizen, so the program should print False.

This program contains exactly one bug. Solution: sol_7_4_1.py
"""

age = 20
is_citizen = False
can_vote = age >= 18 or is_citizen
print(can_vote)   # expected: False
