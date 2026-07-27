"""Solution 16.1.3 — Counting jellybeans

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

There is no break after a successful read, so even on valid input the
while True loop never ends — it keeps re-asking forever. Add break once
a valid count is printed.

Exercise: ex_16_1_3.py
"""

while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
        break
    except ValueError:
        print("Please type a whole number.")
