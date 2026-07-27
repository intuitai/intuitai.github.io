"""Solution 5.4.2 — Shouting

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

word.upper refers to the method without calling it, so it prints a
method object, not the text. Add parentheses to call it: word.upper().

Exercise: ex_5_4_2.py
"""

word = "hello"
loud = word.upper()
print(loud)   # HELLO
