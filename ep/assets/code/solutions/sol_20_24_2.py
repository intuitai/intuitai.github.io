"""Solution 20.24.2 — Final price after discount

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

A percentage must be divided by 100 first; price * 20 computes a huge
discount. Divide the percent by 100 (or test the discount step alone to
catch this).

Exercise: ex_20_24_2.py
"""

def final_price(price, percent_off):
    discount = price * percent_off / 100
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
