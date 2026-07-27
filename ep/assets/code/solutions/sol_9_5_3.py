"""Solution 9.5.3 — Counting down

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

To count downward, range needs a negative step; range(5, 0) counts *up*
and produces nothing because 5 is already past 0. Use range(5, 0, -1).

Exercise: ex_9_5_3.py
"""

for number in range(5, 0, -1):
    print(number)
