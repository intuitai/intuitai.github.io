"""Solution 11.4.1 — declaring global

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

Without a global declaration, assigning visitors makes it local, so
reading it on the right-hand side raises UnboundLocalError. Declare
global visitors so the module-level variable is updated.

Exercise: ex_11_4_1.py
"""

visitors = 0

def arrive():
    global visitors
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
