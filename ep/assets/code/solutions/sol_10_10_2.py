"""Solution 10.10.2 — Sorting with a key

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The key -len(w) sorts longest first; for shortest first the key should
be len(w).

Exercise: ex_10_10_2.py
"""

words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'pear', 'banana']
