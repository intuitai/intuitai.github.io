"""Solution 5.1.4 — Counting by tens

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

"10" is a string, so count + "10" raises a TypeError (you cannot add an
int and a str). Use the int literal 10.

Exercise: ex_5_1_4.py
"""

count = 100
count = count + 10
print(count)   # 110
