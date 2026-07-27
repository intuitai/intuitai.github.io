"""Solution 10.3.3 — Returning early

Chapter 10: Functions — Everyday Programming

Bug type: Logical

A bare return exits immediately and yields None; the formula on the next
line never runs. Put the expression on the return line.

Exercise: ex_10_3_3.py
"""

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
