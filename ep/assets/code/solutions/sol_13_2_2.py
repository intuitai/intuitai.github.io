"""Solution 13.2.2 — Calling with the module prefix

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

With import geometry, the function must be called through its module as
geometry.rectangle_area(...); the bare name rectangle_area is undefined
and raises NameError. Add the module prefix.

Exercise: ex_13_2_2.py
"""

# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(geometry.rectangle_area(4, 6))   # 24
