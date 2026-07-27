"""Exercise 7.5.1 — Vowel check

Chapter 7: Operators — Everyday Programming

This program should report whether the letter is a vowel and print True.

This program contains exactly one bug. Solution: sol_7_5_1.py
"""

letter = "e"
vowels = "aeiou"
is_vowel = letter not in vowels
print(is_vowel)   # expected: True
