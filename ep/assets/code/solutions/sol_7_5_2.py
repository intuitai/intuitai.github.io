"""Solution 7.5.2 — Odd number not in list

Chapter 7: Operators — Everyday Programming

Bug type: Syntax

The membership operator is the two-word phrase not in, written in that
order; in not will not parse. Use not in so a value absent from the list
yields True.

Exercise: ex_7_5_2.py
"""

even_numbers = [2, 4, 6, 8]
number = 7
result = number not in even_numbers
print(result)   # True
