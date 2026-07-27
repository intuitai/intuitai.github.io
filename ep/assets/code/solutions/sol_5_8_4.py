"""Solution 5.8.4 — Shared subjects

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

| is union (all subjects from both); shared items need intersection &.
Use maya & leo to get just {"math"}.

Exercise: ex_5_8_4.py
"""

maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya & leo
print(shared)   # {'math'}
