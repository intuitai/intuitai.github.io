"""Solution 13.2.4 — Spelling the function name

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

The call misspells the function as square_permieter; the module shapes
has no such attribute, so it raises AttributeError. Spell it
square_perimeter to match the definition.

Exercise: ex_13_2_4.py
"""

# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_perimeter(5))   # 20
