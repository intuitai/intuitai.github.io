"""Solution 20.13.2 — Fixing a typo in a word

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

You cannot assign to a single character of a string; word[1] = "e"
raises TypeError. Rebuild the word from slices.

Exercise: ex_20_13_2.py
"""

word = "hpllo"
word = word[0] + "e" + word[2:]
print(word)
