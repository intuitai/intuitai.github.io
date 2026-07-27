"""Solution 16.1.2 — Parsing a price

Chapter 16: Handling Failures — Everyday Programming

Bug type: Runtime

The exception name is misspelled VlaueError, which Python treats as an
unknown name; when float raises the real ValueError it is not caught and
the program crashes (and the wrong name itself raises NameError). Spell
it ValueError.

Exercise: ex_16_1_2.py
"""

try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except ValueError:
    print("That was not a valid price.")
