"""Solution 20.21.4 — Doubling each measurement

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

range(len(...)) makes m the index 0, 1, 2, so it doubles indexes, not
values. Iterate over the measurements directly.

Exercise: ex_20_21_4.py
"""

measurements = [3, 5, 8]
for m in measurements:
    print(m * 2)
