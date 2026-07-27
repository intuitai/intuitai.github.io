"""Solution 18.3.3 — Counting to ten

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

range(1, 10) stops at 9 because the upper bound is excluded, so 10 is
never printed (an off-by-one error). Using range(1, 11) includes 10.

Exercise: ex_18_3_3.py
"""

for number in range(1, 11):
    print(number)
