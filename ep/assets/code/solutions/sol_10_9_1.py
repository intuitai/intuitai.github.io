"""Solution 10.9.1 — Collecting positionals

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

Without a *, args is a single parameter, so passing three numbers raises
a TypeError. Add the star to collect them into a tuple.

Exercise: ex_10_9_1.py
"""

def total(*args):
    return sum(args)

print(total(90, 85, 95))  # 270
