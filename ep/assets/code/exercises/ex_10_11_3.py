"""Exercise 10.11.3 — Guarding the default

Chapter 10: Functions — Everyday Programming

The guard should replace the shared default with a new list when none is
given.

This program contains exactly one bug. Solution: sol_10_11_3.py
"""

def add_score(score, scores=None):
    if scores is None:
        scores = scores
    scores.append(score)
    return scores

print(add_score(90))  # [90]
