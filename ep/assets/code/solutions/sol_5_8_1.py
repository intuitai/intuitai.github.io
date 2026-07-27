"""Solution 5.8.1 — Unique colors

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Square brackets create a list, which keeps the duplicate "red", so len
is 4. Use curly braces to make a set, which drops duplicates and gives
3.

Exercise: ex_5_8_1.py
"""

colors = {"red", "blue", "red", "green"}
print(len(colors))   # 3
