"""Solution 9.4.5 — Largest measurement

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The comparison < keeps the smallest value, not the largest. To track the
maximum, replace it when the current value is *greater*, using >.

Exercise: ex_9_4_5.py
"""

distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance > largest:
        largest = distance

print(largest)
