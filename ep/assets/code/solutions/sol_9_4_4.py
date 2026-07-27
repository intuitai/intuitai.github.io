"""Solution 9.4.4 — Average of readings

Chapter 9: Control Flow — Everyday Programming

Bug type: Runtime

len(reading) uses the loop variable (the last item, an integer) instead
of the list, raising a TypeError. Use len(readings).

Exercise: ex_9_4_4.py
"""

readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(readings)
print(average)
