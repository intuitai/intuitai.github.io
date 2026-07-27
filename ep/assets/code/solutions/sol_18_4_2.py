"""Solution 18.4.2 — Circle circumference

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Printing the returned value shows it is half the expected size: the
formula omits the factor of 2 (circumference is 2 * pi * radius). Adding
the 2 corrects it.

Exercise: ex_18_4_2.py
"""

def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

print(circumference(5))   # about 31.4
