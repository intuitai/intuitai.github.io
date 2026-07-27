"""Exercise 16.1.3 — Counting jellybeans

Chapter 16: Handling Failures — Everyday Programming

This program reads how many jellybeans are in a jar and prints the
count, retrying on bad input.

This program contains exactly one bug. Solution: sol_16_1_3.py
"""

while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
    except ValueError:
        print("Please type a whole number.")
