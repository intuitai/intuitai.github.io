"""Exercise 11.3.3 — counting without touching the global

Chapter 11: Scoping — Everyday Programming

This program should count items in a basket using a local tally and
print the count, leaving the global count at 0.

This program contains exactly one bug. Solution: sol_11_3_3.py
"""

count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + item
    return count

print("Items:", tally())
# Expected:
# Items: 3
