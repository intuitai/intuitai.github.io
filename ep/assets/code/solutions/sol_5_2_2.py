"""Solution 5.2.2 — Splitting a bill

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

// discards the fractional part, giving 12 instead of 12.5. Use true
division / so the result is a float.

Exercise: ex_5_2_2.py
"""

bill = 50
people = 4

each = bill / people
print(each)   # 12.5
