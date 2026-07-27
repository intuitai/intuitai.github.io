"""Solution 13.2.3 — The main guard

Chapter 13: Modules — Everyday Programming

Bug type: Syntax

The guard uses a single = (assignment) instead of == (comparison), which
is a syntax error inside an if condition. Use == to compare __name__
with "__main__".

Exercise: ex_13_2_3.py
"""

# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(c_to_f(100))   # 212.0
