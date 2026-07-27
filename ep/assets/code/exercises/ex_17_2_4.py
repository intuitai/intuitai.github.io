"""Exercise 17.2.4 — Counting even numbers

Chapter 17: Testing — Everyday Programming

This pytest function should confirm that there are 3 even numbers in the
list [1, 2, 3, 4, 6].

This program contains exactly one bug. Solution: sol_17_2_4.py
"""

def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def check_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
