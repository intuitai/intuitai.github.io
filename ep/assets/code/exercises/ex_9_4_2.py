"""Exercise 9.4.2 — Counting vowels

Chapter 9: Control Flow — Everyday Programming

This program should count the vowels in a word. For "education" it
should print 5.

This program contains exactly one bug. Solution: sol_9_4_2.py
"""

word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count + 1)
# Expected: 5
