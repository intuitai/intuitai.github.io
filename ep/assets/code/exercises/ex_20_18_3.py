"""Exercise 20.18.3 — Recording a high score

Chapter 20: Common Pitfalls — Everyday Programming

This program should save the player's high score to disk safely.

This program contains exactly one bug. Solution: sol_20_18_3.py
"""

high_score = 4200
score_file = open("highscore.txt", "w")
score_file.write(str(high_score))
print("High score recorded")
