"""Solution 11.4.2 — global then assign

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

score == 100 is a comparison, not an assignment, so the global is never
changed and stays 0. Use = to assign.

Exercise: ex_11_4_2.py
"""

score = 0

def set_perfect():
    global score
    score = 100

set_perfect()
print("Score:", score)
