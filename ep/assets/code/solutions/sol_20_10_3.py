"""Solution 20.10.3 — Filling in a weekly total

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Index 3 is past the end of a three-item list, so the assignment raises
IndexError. Use append to extend the list.

Exercise: ex_20_10_3.py
"""

weekly_sales = [100, 120, 90]
weekly_sales.append(110)
print(weekly_sales)
