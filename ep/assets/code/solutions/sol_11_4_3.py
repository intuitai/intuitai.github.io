"""Solution 11.4.3 — global keyword spelling

Chapter 11: Scoping — Everyday Programming

Bug type: Syntax

The keyword is global (lowercase); Global is not a keyword, so the line
fails to parse. Use the lowercase keyword.

Exercise: ex_11_4_3.py
"""

temperature = 0

def set_room():
    global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
