"""Exercise 11.5.4 — which scope nonlocal targets

Chapter 11: Scoping — Everyday Programming

This program steps a value upward by 5 each call using nonlocal, and
should print 5 then 10.

This program contains exactly one bug. Solution: sol_11_5_4.py
"""

def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(steper())
print(stepper())
# Expected:
# 5
# 10
