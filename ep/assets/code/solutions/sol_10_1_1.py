"""Solution 10.1.1 — Defining and calling

Chapter 10: Functions — Everyday Programming

Bug type: Logical

Writing welcome only refers to the function object; it does not run it.
You must add parentheses to call it, welcome(), so the body executes.

Exercise: ex_10_1_1.py
"""

def welcome():
    print("Welcome to the science club!")

welcome()
