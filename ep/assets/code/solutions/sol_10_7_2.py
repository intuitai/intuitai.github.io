"""Solution 10.7.2 — Forgetting to return

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The function computes answer but never returns it, so it returns None
and prints None. Add a return.

Exercise: ex_10_7_2.py
"""

def double(number):
    answer = number * 2
    return answer

print(double(7))  # 14
