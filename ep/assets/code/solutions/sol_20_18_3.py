"""Solution 20.18.3 — Recording a high score

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

score_file is opened but never closed. Use with open(...) so the file
closes automatically after writing.

Exercise: ex_20_18_3.py
"""

high_score = 4200
with open("highscore.txt", "w") as score_file:
    score_file.write(str(high_score))
print("High score recorded")
