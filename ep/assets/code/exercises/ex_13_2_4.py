"""Exercise 13.2.4 — Spelling the function name

Chapter 13: Modules — Everyday Programming

This two-file program should print the perimeter of a square with side 5
(20).

This program contains exactly one bug. Solution: sol_13_2_4.py
"""

# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_permieter(5))   # 20
