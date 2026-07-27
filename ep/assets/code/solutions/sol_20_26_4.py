"""Solution 20.26.4 — Tracking a player's scores

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The shared default board=[] keeps old scores between calls. Use None and
create a new list inside the function.

Exercise: ex_20_26_4.py
"""

def new_scoreboard(score, board=None):
    if board is None:
        board = []
    board.append(score)
    return board

print(new_scoreboard(10))  # [10]
print(new_scoreboard(20))  # [20]
