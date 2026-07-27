"""Solution 9.11.3 — First match returns

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The function prints the match instead of returning it, so first_big
returns None. Replacing print with return sends the value back to the
caller.

Exercise: ex_9_11_3.py
"""

def first_big(numbers):
    for number in numbers:
        if number > 10:
            return number

print(first_big([4, 15, 22]))
