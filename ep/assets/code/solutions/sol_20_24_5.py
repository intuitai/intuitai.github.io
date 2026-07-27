"""Solution 20.24.5 — Average of a list of grades

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The stray - 1 skews the average. Testing the bare sum / len step alone
would expose it; remove the - 1.

Exercise: ex_20_24_5.py
"""

def average(grades):
    return sum(grades) / len(grades)

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
