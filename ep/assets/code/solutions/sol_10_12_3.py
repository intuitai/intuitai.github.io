"""Solution 10.12.3 — Integers are immutable

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The global line makes the function overwrite the caller's score, so it
prints 15. An integer is passed by sharing: reassigning the local value
never affects the caller. Drop the global line and work with the
parameter.

Exercise: ex_10_12_3.py
"""

def add_ten(value):
    value = value + 10

score = 5
add_ten(score)
print(score)   # 5
