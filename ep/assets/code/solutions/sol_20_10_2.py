"""Solution 20.10.2 — Recording a new score

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

scores[3] does not exist yet, so assigning to it raises IndexError. Use
append to add the new score.

Exercise: ex_20_10_2.py
"""

scores = [10, 15, 20]
scores.append(25)
print(scores)
