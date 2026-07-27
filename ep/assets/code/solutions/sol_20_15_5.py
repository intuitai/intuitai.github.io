"""Solution 20.15.5 — Greeting the next runner

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

message = greet_runner stores the function, so the print shows a
function object. Call it with an argument.

Exercise: ex_20_15_5.py
"""

def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner("Sam")
print(message)
