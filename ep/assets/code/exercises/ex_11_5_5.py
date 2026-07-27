"""Exercise 11.5.5 — nonlocal vs global

Chapter 11: Scoping — Everyday Programming

This program counts how many times a nested function runs using nonlocal
on the enclosing times, and should print 2.

This program contains exactly one bug. Solution: sol_11_5_5.py
"""

def make_logger():
    times = 0

    def log():
        global times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
# Expected:
# Times: 2
