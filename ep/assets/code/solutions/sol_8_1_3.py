"""Solution 8.1.3 — Printing a shopping list

Chapter 8: Input and Output — Everyday Programming

Bug type: Logical

The sep argument controls what goes between the printed items; a single
space produces apple banana cherry, not the comma-separated list that
was wanted. Set sep=", ".

Exercise: ex_8_1_3.py
"""

fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=", ")
