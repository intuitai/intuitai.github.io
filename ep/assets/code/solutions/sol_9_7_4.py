"""Solution 9.7.4 — First even number

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

break runs before the print, so nothing is ever shown. Print the number
first, then break.

Exercise: ex_9_7_4.py
"""

numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
