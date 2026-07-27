"""Solution 11.4.5 — global so the change sticks

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

Python's boolean is True with a capital T; false is not defined, so the
assignment raises NameError. Use True.

Exercise: ex_11_4_5.py
"""

is_open = False

def open_shop():
    global is_open
    is_open = True

open_shop()
print("Open:", is_open)
