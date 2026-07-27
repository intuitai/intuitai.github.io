"""Solution 11.3.1 — assigning makes it local

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

Because total is assigned inside add(), Python treats it as local
everywhere in the function; reading total on the right-hand side before
it has a local value raises UnboundLocalError. Start the local from a
literal instead of the global.

Exercise: ex_11_3_1.py
"""

total = 0

def add():
    total = 10
    print("Inside:", total)

add()
print("Outside:", total)
