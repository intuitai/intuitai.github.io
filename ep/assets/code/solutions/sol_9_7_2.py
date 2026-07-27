"""Solution 9.7.2 — First over budget

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

break is not indented inside the if, so it runs on the very first item
and the loop stops before finding 150. Indenting break under the if
makes it exit only after a match.

Exercise: ex_9_7_2.py
"""

expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
        break
