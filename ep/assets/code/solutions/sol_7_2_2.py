"""Solution 7.2.2 — Counting down rocket seconds

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The line seconds_left =- 3 is parsed as assigning the value -3, not as
subtracting 3. The intended augmented-assignment operator is -=.

Exercise: ex_7_2_2.py
"""

seconds_left = 10
seconds_left -= 3
print(seconds_left)   # 7
