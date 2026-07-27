"""Solution 9.11.5 — Absolute value

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

When the number is not negative there is no return, so the function
falls off the end and returns None. Adding an else (or a final return
number) handles the non-negative case.

Exercise: ex_9_11_5.py
"""

def absolute(number):
    if number < 0:
        return -number
    else:
        return number

print(absolute(7))
