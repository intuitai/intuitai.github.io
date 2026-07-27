"""Solution 6.4.5 — A list method

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

list.remove deletes by *value*, not by index, so tasks.remove(1) looks
for the value 1 and raises a ValueError. To drop the finished task by
value, remove "report" (or use del tasks[1]).

Exercise: ex_6_4_5.py
"""

tasks = ["email", "report", "lunch"]
tasks.remove("report")
print(tasks)   # ['email', 'lunch']
