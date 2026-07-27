"""Solution 8.1.4 — Saving a temperature reading

Chapter 8: Input and Output — Everyday Programming

Bug type: Runtime

The second open uses mode "w" again, which opens the file for writing
(and erases it); calling f.read() on a write-mode file raises
io.UnsupportedOperation. Open it in read mode "r" to read the contents
back.

Exercise: ex_8_1_4.py
"""

with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "r", encoding="utf-8") as f:
    contents = f.read()

print(contents)
