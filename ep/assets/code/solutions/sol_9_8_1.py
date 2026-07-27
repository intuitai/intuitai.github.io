"""Solution 9.8.1 — Skip the empty entries

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

break stops the loop at the first empty string, so "dog" is never
printed. To skip just the empty entries and continue, use continue.

Exercise: ex_9_8_1.py
"""

words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        continue
    print(word)
