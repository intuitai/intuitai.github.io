"""Solution 11.1.4 — the helper's result must come back out

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

edges is a local variable; without a return, the function hands back
None, so result is None. Return the value so it leaves the local scope.

Exercise: ex_11_1_4.py
"""

def perimeter(length, width):
    edges = 2 * (length + width)
    return edges

result = perimeter(5, 3)
print("Perimeter:", result)
