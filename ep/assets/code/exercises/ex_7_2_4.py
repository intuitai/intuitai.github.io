"""Exercise 7.2.4 — Splitting candy among friends

Chapter 7: Operators — Everyday Programming

There are 12 pieces of candy to split evenly among 4 friends. This
program should update the count to pieces-per-friend and print 3.

This program contains exactly one bug. Solution: sol_7_2_4.py
"""

candy = 12
friends = 4
candy /= friends
print(candy)   # expected: 3
