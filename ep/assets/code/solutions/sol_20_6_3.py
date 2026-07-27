"""Solution 20.6.3 — Concatenating a price into a message

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

"...$" + price adds a string and an int, raising TypeError. Wrap price
in str().

Exercise: ex_20_6_3.py
"""

price = 15
message = "Ticket costs $" + str(price)
print(message)
