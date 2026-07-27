"""Solution 5.9.4 — Safe default with get

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Subject (capital S) is undefined, so printing it raises a NameError.
Print the variable subject.

Exercise: ex_5_9_4.py
"""

student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(subject)   # science
