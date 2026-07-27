"""Solution 9.9.4 — Placeholder branch

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

After pass (which does nothing), the indented print(reading) still runs,
so negative readings are printed too. Removing that stray print leaves
the branch as a true placeholder.

Exercise: ex_9_9_4.py
"""

readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
    else:
        print(reading)
