"""Exercise 20.15.2 — Counting words in a sentence

Chapter 20: Common Pitfalls — Everyday Programming

The program should report how many words a sentence contains.

This program contains exactly one bug. Solution: sol_20_15_2.py
"""

def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count)
