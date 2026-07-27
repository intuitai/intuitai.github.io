"""Solution 10.11.4 — Fresh dictionary each time

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The default dictionary is created once and shared, so entries accumulate
across calls. Use None and create a fresh dictionary inside.

Exercise: ex_10_11_4.py
"""

def tally(name, counts=None):
    if counts is None:
        counts = {}
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
