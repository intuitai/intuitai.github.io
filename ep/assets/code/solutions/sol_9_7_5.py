"""Solution 9.7.5 — Stop at zero

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

continue merely skips the 0 and keeps going (printing 3 afterward), but
the loop should stop at 0. Use break.

Exercise: ex_9_7_5.py
"""

readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        break
    print(reading)
