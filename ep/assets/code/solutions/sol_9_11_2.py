"""Solution 9.11.2 — Describe a number

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The negative branch builds the string "negative" but never returns it,
so describe(-3) falls off that branch and returns None. Adding return
fixes it.

Exercise: ex_9_11_2.py
"""

def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(describe(-3))
