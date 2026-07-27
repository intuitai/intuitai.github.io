"""Solution 7.4.1 — Eligible to vote

Chapter 7: Operators — Everyday Programming

Bug type: Logical

Voting requires both conditions, but or returns True when only one
holds, so a non-citizen adult is wrongly allowed. Use and so both age
and citizenship must be satisfied.

Exercise: ex_7_4_1.py
"""

age = 20
is_citizen = False
can_vote = age >= 18 and is_citizen
print(can_vote)   # False
