"""Solution 10.3.2 — Return the right value

Chapter 10: Functions — Everyday Programming

Bug type: Logical

Division binds tighter than addition, so only c is divided by 3. Wrap
the sum in parentheses before dividing.

Exercise: ex_10_3_2.py
"""

def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(80, 90, 100))  # 90.0
