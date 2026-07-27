"""Solution 6.4.3 — Appending to a list

Chapter 6: Objects — Everyday Programming

Bug type: Logical

n + n doubles each number instead of squaring it, so the list comes out
[2, 4, 6, 8, 10]. Squaring with n * n (or n 2) produces the intended [1,
4, 9, 16, 25].

Exercise: ex_6_4_3.py
"""

squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]
