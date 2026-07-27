"""Exercise 11.3.2 — read before assign

Chapter 11: Scoping — Everyday Programming

This program should print the current step number, then set a new local
step. Because step is assigned later in the function, the read at the
top should fail unless it is read from somewhere valid.

This program contains exactly one bug. Solution: sol_11_3_2.py
"""

step = 1

def advance():
    print("Current:", step)
    step = step + 1

advance()
# Expected:
# Current: 1
