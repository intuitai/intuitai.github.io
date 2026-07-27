"""Solution 10.9.4 — Unpacking into a call

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

Passing the list as one argument fills only a, leaving b and c missing,
which raises a TypeError. Unpack with a star: add_three(*numbers).

Exercise: ex_10_9_4.py
"""

def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(*numbers))  # 6
