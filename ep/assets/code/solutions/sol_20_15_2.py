"""Solution 20.15.2 — Counting words in a sentence

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

word_count alone is the function object; it was never called with the
sentence. Call it as word_count(note).

Exercise: ex_20_15_2.py
"""

def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count(note))
