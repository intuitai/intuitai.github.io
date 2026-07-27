"""Exercise 10.9.3 — Keyword collection

Chapter 10: Functions — Everyday Programming

This program should print the keyword arguments as a dictionary.

This program contains exactly one bug. Solution: sol_10_9_3.py
"""

def show_options(*kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
