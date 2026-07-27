"""Solution 5.10.2 — Building a message

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

You cannot concatenate a str and an int, so this raises a TypeError.
Convert the number with str() first.

Exercise: ex_5_10_2.py
"""

score = 90
message = "Score: " + str(score)
print(message)   # Score: 90
