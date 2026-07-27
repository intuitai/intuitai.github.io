"""Solution 16.2.5 — Percent off

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The broad except Exception comes first, and since ZeroDivisionError is a
subclass of Exception, a zero divisor is caught by the first handler and
reported as “not a valid number”; the specific ZeroDivisionError handler
can never run. List the specific handler before the general one.

Exercise: ex_16_2_5.py
"""

price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except ZeroDivisionError:
    print("The divisor cannot be zero.")
except Exception:
    print("That was not a valid number.")
