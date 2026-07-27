"""Solution 9.1.5 — Ticket price by age

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The print is indented inside the else branch, so it only runs for the
full price; the child's price is never shown. Moving print out to run
after the if/else fixes it.

Exercise: ex_9_1_5.py
"""

age = 10

if age < 12:
    price = 5
else:
    price = 12

print("Ticket price:", price)
