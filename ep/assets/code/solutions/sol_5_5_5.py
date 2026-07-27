"""Solution 5.5.5 — Comparing to None

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Not_set (capital N) is undefined, so printing it raises a NameError.
Print the variable not_set.

Exercise: ex_5_5_5.py
"""

username = None
not_set = username is None
print(not_set)   # True
