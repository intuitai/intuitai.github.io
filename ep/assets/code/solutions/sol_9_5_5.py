"""Solution 9.5.5 — Three repetitions

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

range(3) runs three times, but the extra print(count) also prints the
index each pass, which was not intended. Removing that line prints Hello
three times.

Exercise: ex_9_5_5.py
"""

for count in range(3):
    print("Hello")
