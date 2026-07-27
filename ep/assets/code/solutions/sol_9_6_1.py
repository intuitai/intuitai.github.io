"""Solution 9.6.1 — Counting with while

Chapter 9: Control Flow — Everyday Programming

Bug type: Runtime

The loop never updates count, so the condition stays true forever—an
infinite loop. Incrementing count each pass lets it terminate.

Exercise: ex_9_6_1.py
"""

count = 1

while count <= 5:
    print(count)
    count += 1
