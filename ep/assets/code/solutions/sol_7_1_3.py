"""Solution 7.1.3 — Eggs left over

Chapter 7: Operators — Everyday Programming

Bug type: Logical

Floor division // gives the number of full cartons (2), not the leftover
eggs. The remainder operator % gives what is left over.

Exercise: ex_7_1_3.py
"""

total_eggs = 17
carton_size = 6
leftover = total_eggs % carton_size
print(leftover)   # 5
