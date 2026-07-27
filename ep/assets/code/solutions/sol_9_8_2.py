"""Solution 9.8.2 — Skip one value

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

pass does nothing, so 3 is still printed. To actually skip it, use
continue.

Exercise: ex_9_8_2.py
"""

for number in range(1, 7):
    if number == 3:
        continue
    print(number)
