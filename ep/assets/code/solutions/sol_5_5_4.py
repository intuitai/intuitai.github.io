"""Solution 5.5.4 — Length of nothing

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

len(None) raises a TypeError because None has no length. Check for None
first and use 0 in that case.

Exercise: ex_5_5_4.py
"""

temps = None
count = len(temps) if temps is not None else 0
print(count)   # 0
