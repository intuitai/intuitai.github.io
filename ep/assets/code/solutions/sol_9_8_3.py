"""Solution 9.8.3 — Sum positive numbers

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The continue after total += number is harmless, but print(total + 1)
adds an extra 1, giving 10 instead of 9. Printing total gives the
correct sum.

Exercise: ex_9_8_3.py
"""

numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number

print(total)
