"""Solution 10.2.4 — Using the parameter

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The call uses number, a name that exists only inside the function, so
Python raises a NameError. Pass an actual value such as 5.

Exercise: ex_10_2_4.py
"""

def double(number):
    return number * 2

print(double(5))
