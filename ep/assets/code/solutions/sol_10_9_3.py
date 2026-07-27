"""Solution 10.9.3 — Keyword collection

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

A single star collects positional arguments; keyword arguments need two
stars. With one star, the keyword call raises a TypeError. Use kwargs.

Exercise: ex_10_9_3.py
"""

def show_options(**kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
