"""Exercise 20.26.4 — Tracking a player's scores

Chapter 20: Common Pitfalls — Everyday Programming

Each call should start a brand-new scoreboard with just the given score.

This program contains exactly one bug. Solution: sol_20_26_4.py
"""

def new_scoreboard(score, board=[]):
    board.append(score)
    return board

print(new_scoreboard(10))  # expected [10]
print(new_scoreboard(20))  # expected [20]
