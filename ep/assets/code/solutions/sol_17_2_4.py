"""Solution 17.2.4 — Counting even numbers

Chapter 17: Testing — Everyday Programming

Bug type: Logical

pytest only discovers functions whose names start with test_;
check_count_evens will never be collected or run. Renaming it to
test_count_evens lets pytest find it.

Exercise: ex_17_2_4.py
"""

def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def test_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
