"""Solution 10.3.1 — Return, do not print

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The function prints instead of returning, so total becomes None. Use
return so the caller receives the value.

Exercise: ex_10_3_1.py
"""

def add(a, b):
    return a + b

total = add(5, 7)
print(total)  # 12
