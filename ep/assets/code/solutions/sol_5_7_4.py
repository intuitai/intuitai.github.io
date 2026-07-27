"""Solution 5.7.4 — A single value

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

(42) is just the number 42 in parentheses, not a tuple, so len(single)
raises a TypeError on an int. A one-element tuple needs a trailing
comma: (42,).

Exercise: ex_5_7_4.py
"""

single = (42,)
print(len(single))   # 1
