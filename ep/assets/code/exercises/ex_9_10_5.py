"""Exercise 9.10.5 — Traffic light

Chapter 9: Control Flow — Everyday Programming

This program should print the action for a traffic light colour. For an
unknown colour like "blue" it should print Unknown.

This program contains exactly one bug. Solution: sol_9_10_5.py
"""

color = "blue"

match color:
    case "green":
        print("Go")
    case "yellow":
        print("Slow down")
    case "red":
        print("Stop")
    case _:
        "Unknown"
# Expected: Unknown
