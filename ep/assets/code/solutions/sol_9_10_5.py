"""Solution 9.10.5 — Traffic light

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The default case builds the string "Unknown" but never prints it, so an
unrecognized colour produces no output. Adding print produces the
expected output.

Exercise: ex_9_10_5.py
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
        print("Unknown")
