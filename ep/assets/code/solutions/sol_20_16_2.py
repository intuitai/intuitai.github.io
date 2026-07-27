"""Solution 20.16.2 — Averaging three test grades

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The average is computed into average_value but never returned, so None
is printed. Return the value.

Exercise: ex_20_16_2.py
"""

def average(a, b, c):
    total = a + b + c
    average_value = total / 3
    return average_value

print("Average:", average(80, 90, 100))
