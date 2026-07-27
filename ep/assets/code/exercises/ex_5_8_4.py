"""Exercise 5.8.4 — Shared subjects

Chapter 5: Data Structures — Everyday Programming

Two students list their subjects. The program should print the subjects
they share: {"math"}.

This program contains exactly one bug. Solution: sol_5_8_4.py
"""

maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya | leo
print(shared)   # {'math'}
