"""Solution 9.10.4 — Default case

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

case "_" matches the literal string "_", not “anything else”. The
wildcard default is the bare _ with no quotes.

Exercise: ex_9_10_4.py
"""

command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
