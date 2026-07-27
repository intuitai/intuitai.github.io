"""Solution 9.7.1 — Stop at the target

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

continue only skips 3 and keeps going (printing 4, 5), but the program
should stop entirely before 3. Use break to exit the loop.

Exercise: ex_9_7_1.py
"""

for number in range(1, 6):
    if number == 3:
        break
    print(number)
