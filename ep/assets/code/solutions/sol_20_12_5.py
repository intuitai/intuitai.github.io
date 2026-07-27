"""Solution 20.12.5 — A list of scores to extend

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Parentheses create a tuple, which has no append, raising AttributeError.
Use brackets to make a list.

Exercise: ex_20_12_5.py
"""

scores = [88, 92]
scores.append(75)
print(scores)
