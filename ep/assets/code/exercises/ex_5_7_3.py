"""Exercise 5.7.3 — Unpacking coordinates

Chapter 5: Data Structures — Everyday Programming

The program should unpack a tuple into two variables and print "lat
35.7, lon 139.7".

This program contains exactly one bug. Solution: sol_5_7_3.py
"""

coords = (35.7, 139.7)
lat = coords
lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
