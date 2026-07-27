"""Solution 16.3.2 — Area of a rectangle

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The else block computes area but never prints it, so the program
produces no visible result on success. Print the area in the else block.

Exercise: ex_16_3_2.py
"""

try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
    print("Area:", area)
