"""Solution 20.8.2 — Pages per chapter

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

52 / 5 is 10.4; the program wants whole pages. Use // for the integer
quotient 10.

Exercise: ex_20_8_2.py
"""

pages = 52
chapters = 5
print(pages // chapters)  # 10
