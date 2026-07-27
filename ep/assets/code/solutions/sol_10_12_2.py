"""Solution 10.12.2 — Rebinding stays local

Chapter 10: Functions — Everyday Programming

Bug type: Logical

clear and extend mutate the shared list in place, so the caller sees
[99, 100], not the original. To leave the caller unchanged, rebind the
local name instead.

Exercise: ex_10_12_2.py
"""

def replace(numbers):
    numbers = [99, 100]

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
