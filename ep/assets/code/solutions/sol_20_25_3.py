"""Solution 20.25.3 — Duplicating a tic-tac-toe board

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

list(board) makes a shallow copy whose inner rows are shared, so editing
trial changes board. Use copy.deepcopy.

Exercise: ex_20_25_3.py
"""

import copy

board = [["X", "O"], ["O", "X"]]
trial = copy.deepcopy(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
