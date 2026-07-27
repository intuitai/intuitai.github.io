"""Exercise 9.3.1 — Entry rules

Chapter 9: Control Flow — Everyday Programming

Entry is allowed only when a person is at least 18 *and* has an ID. With
age 20 and no ID, this should print Entry denied.

This program contains exactly one bug. Solution: sol_9_3_1.py
"""

age = 20
has_id = False

if age >= 18 or has_id:
    print("Entry allowed")
else:
    print("Entry denied")
# Expected: Entry denied
