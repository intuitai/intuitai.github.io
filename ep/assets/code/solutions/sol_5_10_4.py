"""Solution 5.10.4 — Converting to float

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

int("2.5") raises a ValueError because the text is not a whole number.
Use float() to convert it.

Exercise: ex_5_10_4.py
"""

weight_text = "2.5"
weight = float(weight_text)
print(weight * 2)   # 5.0
