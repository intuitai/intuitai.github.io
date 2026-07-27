"""Solution 10.12.1 — Mutating shares the change

Chapter 10: Functions — Everyday Programming

Bug type: Logical

numbers = numbers + [1] builds a new list and rebinds the local name,
leaving the caller's list unchanged. Use append, which mutates the
shared list.

Exercise: ex_10_12_1.py
"""

def add_one(numbers):
    numbers.append(1)

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
