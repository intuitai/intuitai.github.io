"""Solution 5.5.1 — No reading yet

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

None is not the same as the string "None", so the comparison is always
False. Compare to the real None value with is None.

Exercise: ex_5_5_1.py
"""

reading = None
no_data = reading is None
print(no_data)   # True
