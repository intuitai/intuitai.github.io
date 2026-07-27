"""Exercise 9.8.1 — Skip the empty entries

Chapter 9: Control Flow — Everyday Programming

This program should print every non-empty word in the list.

This program contains exactly one bug. Solution: sol_9_8_1.py
"""

words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        break
    print(word)
# Expected: cat dog
