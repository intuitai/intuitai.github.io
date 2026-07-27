"""Solution 5.10.1 — Reading a number

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

age_text is a string, so age_text + 5 mixes str and int and raises a
TypeError. Convert the text with int() before adding.

Exercise: ex_5_10_1.py
"""

age_text = "25"
age = int(age_text) + 5
print(age)   # 30
