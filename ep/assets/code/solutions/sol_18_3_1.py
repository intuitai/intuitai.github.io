"""Solution 18.3.1 — Rectangle area

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

The program runs but uses + where area requires multiplication, so it
returns 10 instead of 24. Multiplying length by width gives the correct
area.

Exercise: ex_18_3_1.py
"""

def area(length, width):
    return length * width

print(area(6, 4))   # 24
