"""Solution 10.7.5 — Expecting a value

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The function assigns chosen but never returns it, so number is None.
Return chosen.

Exercise: ex_10_7_5.py
"""

def lucky_number():
    chosen = 42
    return chosen

number = lucky_number()
print(number)  # 42
