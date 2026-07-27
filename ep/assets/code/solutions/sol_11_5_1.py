"""Solution 11.5.1 — nonlocal counter

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

Assigning count inside increment() makes it local, so count + 1 reads a
local with no value — UnboundLocalError. Declare nonlocal count to
target the enclosing variable.

Exercise: ex_11_5_1.py
"""

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
