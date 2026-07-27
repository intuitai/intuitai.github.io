"""Exercise 13.1.4 — Average test score

Chapter 13: Modules — Everyday Programming

This program should print the average of four test scores using the
statistics module.

This program contains exactly one bug. Solution: sol_13_1_4.py
"""

import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistic.mean(scores))   # expected: 85
