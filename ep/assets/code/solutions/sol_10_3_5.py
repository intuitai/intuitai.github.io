"""Solution 10.3.5 — Use the returned value

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The returned value is discarded and area is never defined, so printing
it raises a NameError. Store the result, then print it.

Exercise: ex_10_3_5.py
"""

def square(side):
    return side * side

area = square(6)
print(area)  # 36
