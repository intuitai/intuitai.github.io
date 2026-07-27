"""Solution 10.6.3 — Matching the count

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function returns three values but only two names receive them,
raising a ValueError. Return just the two values you unpack.

Exercise: ex_10_6_3.py
"""

def person():
    return "Luis", 14

name, age = person()
print(name, age)  # Luis 14
