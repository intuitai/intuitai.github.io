"""Solution 10.5.5 — Mixing names and positions

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

time=3 is an unexpected keyword the function does not accept, raising a
TypeError. Pass only the three real parameters.

Exercise: ex_10_5_5.py
"""

def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02))  # 60.0
