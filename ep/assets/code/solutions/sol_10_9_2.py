"""Solution 10.9.2 — The star on args

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

args without a star accepts only one argument, so passing three raises a
TypeError. Use *args to gather them.

Exercise: ex_10_9_2.py
"""

def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
