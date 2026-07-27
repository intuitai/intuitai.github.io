"""Solution 8.1.1 — Doubling a recipe

Chapter 8: Input and Output — Everyday Programming

Bug type: Logical

input() always returns a string, so cookies * 2 repeats the text
("1212") instead of computing 24. Convert the input to an int before
doing arithmetic.

Exercise: ex_8_1_1.py
"""

# Assume the user types: 12
cookies = int(input("How many cookies does the recipe make? "))
print(f"Doubled, that is {cookies * 2} cookies.")
