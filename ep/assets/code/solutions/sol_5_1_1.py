"""Solution 5.1.1 — Total points

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The third section was subtracted instead of added, giving 25 instead of
75. Change the - to + so all three sections are summed.

Exercise: ex_5_1_1.py
"""

section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 + section3
print(total)   # 75
