"""Solution 7.5.1 — Vowel check

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The code used not in, which would report False for a real vowel. To
confirm membership, use the in operator.

Exercise: ex_7_5_1.py
"""

letter = "e"
vowels = "aeiou"
is_vowel = letter in vowels
print(is_vowel)   # True
