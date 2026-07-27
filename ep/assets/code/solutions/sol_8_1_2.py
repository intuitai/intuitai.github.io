"""Solution 8.1.2 — Average of two test scores

Chapter 8: Input and Output — Everyday Programming

Bug type: Logical

Without parentheses, score1 + score2 / 2 divides only the second score
first (operator precedence), giving 125.0 instead of 85.0. Parenthesize
the sum before dividing.

Exercise: ex_8_1_2.py
"""

# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = (score1 + score2) / 2
print(f"Your average is {average}.")
