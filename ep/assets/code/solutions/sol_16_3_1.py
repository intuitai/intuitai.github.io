"""Solution 16.3.1 — Confirming a conversion

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The success line is printed twice — once inside try and again in else.
Code that should run only on success belongs in else, not in try; remove
the duplicate from the try block.

Exercise: ex_16_3_1.py
"""

text = "42"
try:
    number = int(text)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
