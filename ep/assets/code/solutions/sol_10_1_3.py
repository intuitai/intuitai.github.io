"""Solution 10.1.3 — The function body

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The body must be indented under the def line. An unindented print makes
Python expect an indented block and raises an IndentationError.

Exercise: ex_10_1_3.py
"""

def days_in_week():
    print("A week has 7 days.")

days_in_week()
