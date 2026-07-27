---
title: "Chapter 8: Input and Output — Solutions"
short_title: "Ch. 8 — Input and Output"
layout: post
permalink: /ep/solutions/08-input-and-output/
order: 4
chapter: 8
---

Worked solutions to the 5 *Find the Bug* exercises in [Chapter 8: Input and Output]({{ site.baseurl }}/ep/exercises/08-input-and-output/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 8.1.1–8.1.5

### Solution 8.1.1 — Doubling a recipe
{: #sol-8-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`input()` always returns a string, so `cookies * 2` repeats the text (`"1212"`) instead of computing `24`. Convert the input to an `int` before doing arithmetic.

```python
# Assume the user types: 12
cookies = int(input("How many cookies does the recipe make? "))
print(f"Doubled, that is {cookies * 2} cookies.")
```

[Back to Exercise 8.1.1]({{ site.baseurl }}/ep/exercises/08-input-and-output/#ex-8-1-1) &middot; [`sol_8_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_8_1_1.py)

</details>

### Solution 8.1.2 — Average of two test scores
{: #sol-8-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Without parentheses, `score1 + score2 / 2` divides only the second score first (operator precedence), giving 125.0 instead of 85.0. Parenthesize the sum before dividing.

```python
# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = (score1 + score2) / 2
print(f"Your average is {average}.")
```

[Back to Exercise 8.1.2]({{ site.baseurl }}/ep/exercises/08-input-and-output/#ex-8-1-2) &middot; [`sol_8_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_8_1_2.py)

</details>

### Solution 8.1.3 — Printing a shopping list
{: #sol-8-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `sep` argument controls what goes between the printed items; a single space produces `apple banana cherry`, not the comma-separated list that was wanted. Set `sep=", "`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=", ")
```

[Back to Exercise 8.1.3]({{ site.baseurl }}/ep/exercises/08-input-and-output/#ex-8-1-3) &middot; [`sol_8_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_8_1_3.py)

</details>

### Solution 8.1.4 — Saving a temperature reading
{: #sol-8-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The second `open` uses mode `"w"` again, which opens the file for writing (and erases it); calling `f.read()` on a write-mode file raises `io.UnsupportedOperation`. Open it in read mode `"r"` to read the contents back.

```python
with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "r", encoding="utf-8") as f:
    contents = f.read()

print(contents)
```

[Back to Exercise 8.1.4]({{ site.baseurl }}/ep/exercises/08-input-and-output/#ex-8-1-4) &middot; [`sol_8_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_8_1_4.py)

</details>

### Solution 8.1.5 — Greeting by name
{: #sol-8-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The f-string is missing its closing double quote, so Python never finds the end of the string and reports a syntax error. Add the closing `"` before the parenthesis.

```python
# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.")
```

[Back to Exercise 8.1.5]({{ site.baseurl }}/ep/exercises/08-input-and-output/#ex-8-1-5) &middot; [`sol_8_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_8_1_5.py)

</details>

