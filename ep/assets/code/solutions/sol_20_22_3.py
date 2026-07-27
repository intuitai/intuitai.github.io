"""Solution 20.22.3 — Turning a word into letters

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

list = "abc" shadows the built-in list, so list("hello") tries to call a
string and raises TypeError. Rename the variable.

Exercise: ex_20_22_3.py
"""

word = "abc"
letters = list("hello")
print(letters)
