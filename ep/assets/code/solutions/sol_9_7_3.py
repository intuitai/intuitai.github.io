"""Solution 9.7.3 — Search for a name

Chapter 9: Control Flow — Everyday Programming

Bug type: Runtime

brake is a misspelling of break, so Python raises a NameError.
Correcting the keyword fixes it.

Exercise: ex_9_7_3.py
"""

names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        break
