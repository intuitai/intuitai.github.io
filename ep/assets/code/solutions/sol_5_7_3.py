"""Solution 5.7.3 — Unpacking coordinates

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Assigning the whole tuple to each name does not unpack it. Unpack both
values at once with lat, lon = coords.

Exercise: ex_5_7_3.py
"""

coords = (35.7, 139.7)
lat, lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
