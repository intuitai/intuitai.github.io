"""Solution 10.11.3 — Guarding the default

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The guard assigns scores = scores, leaving it None, so append raises an
AttributeError. Assign a new empty list instead.

Exercise: ex_10_11_3.py
"""

def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(90))  # [90]
