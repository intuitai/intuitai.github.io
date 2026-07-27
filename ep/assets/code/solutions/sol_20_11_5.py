"""Solution 20.11.5 — Looping one step too far

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

index <= len(prices) lets index reach 3, which is out of range, so the
loop raises IndexError. Stop with < instead of <=.

Exercise: ex_20_11_5.py
"""

prices = [3, 5, 9]
index = 0
while index < len(prices):
    print(prices[index])
    index = index + 1
