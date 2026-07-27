"""Solution 9.3.1 — Entry rules

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

or allows entry when *either* condition holds, but both age and ID are
required. Using and enforces both.

Exercise: ex_9_3_1.py
"""

age = 20
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
