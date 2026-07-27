"""Solution 20.6.5 — Treating a string as a number

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime/Logical

score holds the text "75", so score + 10 mixes a string and an int and
raises TypeError. Convert score to an integer (or store it as one)
before adding.

Exercise: ex_20_6_5.py
"""

score = int("75")
print(score + 10)
