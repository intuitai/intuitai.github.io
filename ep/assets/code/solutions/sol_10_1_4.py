"""Solution 10.1.4 — Indenting the body

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The two body lines must share the same indentation. The second print is
indented two spaces instead of four, so Python raises an
IndentationError.

Exercise: ex_10_1_4.py
"""

def study_plan():
    print("Read the chapter.")
    print("Solve five problems.")

study_plan()
