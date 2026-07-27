"""Solution 5.9.5 — Adding an entry

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

== compares values; it does not store anything, so the key "phone" is
never added and the next line raises a KeyError. Use a single = to
assign the new entry.

Exercise: ex_5_9_5.py
"""

contact = {"name": "Leo"}
contact["phone"] = "555-0100"
print(contact["phone"])   # 555-0100
