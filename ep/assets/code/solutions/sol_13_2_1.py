"""Solution 13.2.1 — Importing your own helper

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

The import line asks for c_to_k, but conversions.py only defines c_to_f,
so the import raises ImportError. Import the function that actually
exists.

Exercise: ex_13_2_1.py
"""

# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_f

print(c_to_f(100))   # 212.0
