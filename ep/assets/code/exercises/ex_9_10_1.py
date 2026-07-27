"""Exercise 9.10.1 — Matching a command

Chapter 9: Control Flow — Everyday Programming

This program should respond to a command. For "start" it should print
Starting....

This program contains exactly one bug. Solution: sol_9_10_1.py
"""

command = "start"

match command:
    case "start"
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
