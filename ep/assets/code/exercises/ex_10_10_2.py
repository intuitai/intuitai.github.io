"""Exercise 10.10.2 — Sorting with a key

Chapter 10: Functions — Everyday Programming

This should sort the words from shortest to longest.

This program contains exactly one bug. Solution: sol_10_10_2.py
"""

words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: -len(w)))
# ['fig', 'pear', 'banana']
