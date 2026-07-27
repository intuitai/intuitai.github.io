"""Solution 18.4.3 — Sum of a list

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Printing total inside the loop shows it only ever holds the latest
value: the line replaces the running sum instead of adding to it. Using
+= accumulates the total.

Exercise: ex_18_4_3.py
"""

rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total += amount
print(total)   # 5.5
