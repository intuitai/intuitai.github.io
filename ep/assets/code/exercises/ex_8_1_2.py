"""Exercise 8.1.2 — Average of two test scores

Chapter 8: Input and Output — Everyday Programming

Assuming the user types 80 then 90, this program should print Your
average is 85.0..

This program contains exactly one bug. Solution: sol_8_1_2.py
"""

# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = score1 + score2 / 2
print(f"Your average is {average}.")
