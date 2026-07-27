"""Solution 5.4.4 — Length of a word

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

word() tries to call the string as if it were a function, raising a
TypeError. Pass the string itself to len.

Exercise: ex_5_4_4.py
"""

word = "science"
count = len(word)
print(count)   # 7
