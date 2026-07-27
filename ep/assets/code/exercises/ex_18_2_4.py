"""Exercise 18.2.4 — Last student's score

Chapter 18: Bugs — Everyday Programming

This program should print the score of the last student in the list.

This program contains exactly one bug. Solution: sol_18_2_4.py
"""

scores = [88, 91, 79, 95]
last_index = len(scores)
print(scores[last_index])   # expected: 95
