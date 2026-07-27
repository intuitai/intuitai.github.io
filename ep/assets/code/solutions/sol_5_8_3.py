"""Solution 5.8.3 — Is it a member?

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The program tests "yellow", which is not in the set, so it prints False.
Test for "blue" to get True.

Exercise: ex_5_8_3.py
"""

colors = {"red", "blue", "green"}
print("blue" in colors)   # True
