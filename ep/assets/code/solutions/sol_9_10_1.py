"""Solution 9.10.1 — Matching a command

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

The first case line is missing its colon. Adding it fixes the parse.

Exercise: ex_9_10_1.py
"""

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
