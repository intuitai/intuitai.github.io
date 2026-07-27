"""Exercise 10.11.4 — Fresh dictionary each time

Chapter 10: Functions — Everyday Programming

Each call should return a dictionary with just one entry.

This program contains exactly one bug. Solution: sol_10_11_4.py
"""

def tally(name, counts={}):
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
