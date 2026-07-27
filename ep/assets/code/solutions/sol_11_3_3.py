"""Solution 11.3.3 — counting without touching the global

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The local count should be increased by 1 per item, but count + item adds
a string to an integer and raises TypeError. Increment by 1 instead.

Exercise: ex_11_3_3.py
"""

count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + 1
    return count

print("Items:", tally())
