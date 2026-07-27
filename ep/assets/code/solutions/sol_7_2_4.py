"""Solution 7.2.4 — Splitting candy among friends

Chapter 7: Operators — Everyday Programming

Bug type: Logical

/= performs true division and produces 3.0, a float, instead of the
whole number 3. Use floor-division assignment //= to keep an integer
count of pieces per friend.

Exercise: ex_7_2_4.py
"""

candy = 12
friends = 4
candy //= friends
print(candy)   # 3
