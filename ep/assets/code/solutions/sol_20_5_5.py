"""Solution 20.5.5 — Misspelled list name

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

score (singular) was never defined; the list is named scores, so
sum(score) raises NameError. Pass the correct list name.

Exercise: ex_20_5_5.py
"""

scores = [80, 90, 100]
average = sum(scores) / len(scores)
print(average)  # 90.0
