"""Solution 9.4.2 — Counting vowels

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The count is correct, but print(count + 1) adds one extra at the end.
Print count itself.

Exercise: ex_9_4_2.py
"""

word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count)
