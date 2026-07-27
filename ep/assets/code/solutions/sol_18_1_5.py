"""Solution 18.1.5 — Counting change

Chapter 18: Bugs — Everyday Programming

Bug type: Syntax

The print line is not indented under the for, so Python raises an
IndentationError because a loop body is expected. Indenting the line by
four spaces puts it inside the loop.

Exercise: ex_18_1_5.py
"""

coins = [25, 10, 5, 1]
for coin in coins:
    print(coin)
