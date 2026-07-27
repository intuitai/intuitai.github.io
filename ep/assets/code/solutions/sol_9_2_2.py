"""Solution 9.2.2 — Freezing point

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

< excludes 0 itself, but water freezes *at* 0 too. Using <= includes the
freezing point.

Exercise: ex_9_2_2.py
"""

temp_c = 0

if temp_c <= 0:
    print("Frozen")
else:
    print("Liquid")
