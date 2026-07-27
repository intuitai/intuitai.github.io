"""Solution 20.21.2 — Summing daily sales

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

total + sales adds an integer to the whole list, raising TypeError.
Iterate over the items and add each value.

Exercise: ex_20_21_2.py
"""

sales = [120, 85, 200, 95]
total = 0
for amount in sales:
    total = total + amount
print("Total sales:", total)
