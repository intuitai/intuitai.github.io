"""Solution 20.15.3 — Rolling for a starting number

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

score = starting_score stores the function itself, not its result. Add
() to call it.

Exercise: ex_20_15_3.py
"""

def starting_score():
    return 100

score = starting_score()
print("You begin with", score, "points")
