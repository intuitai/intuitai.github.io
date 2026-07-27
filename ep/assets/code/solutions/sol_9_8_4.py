"""Solution 9.8.4 — Skip the indentation

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

The continue under the if is not indented, so Python raises an
IndentationError. Indenting it inside the if fixes the parse.

Exercise: ex_9_8_4.py
"""

for number in range(1, 7):
    if number % 2 == 0:
        continue
    print(number)
