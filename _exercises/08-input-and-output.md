---
title: "Chapter 8: Input and Output"
short_title: "Ch. 8 — Input and Output"
layout: post
permalink: /ep/exercises/08-input-and-output/
order: 4
chapter: 8
exercise_count: 5
---

5 *Find the Bug* exercises from Chapter 8 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 8 solutions]({{ site.baseurl }}/ep/solutions/08-input-and-output/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 8.1.1–8.1.5

### Exercise 8.1.1 — Doubling a recipe
{: #ex-8-1-1 }

This program asks how many cookies a recipe makes, then prints double that amount.

```python
# Assume the user types: 12
cookies = input("How many cookies does the recipe make? ")
print(f"Doubled, that is {cookies * 2} cookies.")
```

[Solution 8.1.1]({{ site.baseurl }}/ep/solutions/08-input-and-output/#sol-8-1-1) &middot; [`ex_8_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_8_1_1.py)

### Exercise 8.1.2 — Average of two test scores
{: #ex-8-1-2 }

Assuming the user types 80 then 90, this program should print `Your average is 85.0.`.

```python
# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = score1 + score2 / 2
print(f"Your average is {average}.")
```

[Solution 8.1.2]({{ site.baseurl }}/ep/solutions/08-input-and-output/#sol-8-1-2) &middot; [`ex_8_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_8_1_2.py)

### Exercise 8.1.3 — Printing a shopping list
{: #ex-8-1-3 }

This program should print three fruits on one line, separated by commas, like `apple, banana, cherry`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=" ")
```

[Solution 8.1.3]({{ site.baseurl }}/ep/solutions/08-input-and-output/#sol-8-1-3) &middot; [`ex_8_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_8_1_3.py)

### Exercise 8.1.4 — Saving a temperature reading
{: #ex-8-1-4 }

This program writes one weather reading to a file and then prints it back.

```python
with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "w", encoding="utf-8") as f:
    contents = f.read()

print(contents)
```

[Solution 8.1.4]({{ site.baseurl }}/ep/solutions/08-input-and-output/#sol-8-1-4) &middot; [`ex_8_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_8_1_4.py)

### Exercise 8.1.5 — Greeting by name
{: #ex-8-1-5 }

This program asks for a name and prints a greeting.

```python
# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.)
```

[Solution 8.1.5]({{ site.baseurl }}/ep/solutions/08-input-and-output/#sol-8-1-5) &middot; [`ex_8_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_8_1_5.py)

