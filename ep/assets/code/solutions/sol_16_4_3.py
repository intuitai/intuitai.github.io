"""Solution 16.4.3 — Logging an attempt

Chapter 16: Handling Failures — Everyday Programming

Bug type: Syntax

The finally keyword is missing its colon, so the file will not parse.
Add the colon after finally.

Exercise: ex_16_4_3.py
"""

try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally:
    print("Attempt logged.")
