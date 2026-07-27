"""Exercise 20.25.3 — Duplicating a tic-tac-toe board

Chapter 20: Common Pitfalls — Everyday Programming

This program should duplicate a game board so the duplicate can be
edited safely.

This program contains exactly one bug. Solution: sol_20_25_3.py
"""

import copy

board = [["X", "O"], ["O", "X"]]
trial = list(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
