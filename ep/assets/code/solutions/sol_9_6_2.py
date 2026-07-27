"""Solution 9.6.2 — Countdown

Chapter 9: Control Flow — Everyday Programming

Bug type: Runtime

count += 1 moves away from the stop condition, so count > 0 never
becomes false—an infinite loop. Use count -= 1 to count down.

Exercise: ex_9_6_2.py
"""

count = 3

while count > 0:
    print(count)
    count -= 1

print("Liftoff")
