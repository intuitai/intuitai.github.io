"""Solution 5.4.1 — First letter

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

String indexing starts at 0, so city[1] is the second letter ("o"). Use
index 0 for the first letter.

Exercise: ex_5_4_1.py
"""

city = "Tokyo"
first = city[0]
print(first)   # T
