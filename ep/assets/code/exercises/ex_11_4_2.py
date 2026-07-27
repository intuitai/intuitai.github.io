"""Exercise 11.4.2 — global then assign

Chapter 11: Scoping — Everyday Programming

This program should use global to set the module-level score to 100 from
inside the function, and print 100.

This program contains exactly one bug. Solution: sol_11_4_2.py
"""

score = 0

def set_perfect():
    global score
    score == 100

set_perfect()
print("Score:", score)
# Expected:
# Score: 100
