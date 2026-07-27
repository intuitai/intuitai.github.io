---
title: "Chapter 20: Common Pitfalls — Solutions"
short_title: "Ch. 20 — Common Pitfalls"
layout: post
permalink: /ep/solutions/20-common-pitfalls/
order: 12
chapter: 20
---

Worked solutions to the 130 *Find the Bug* exercises in [Chapter 20: Common Pitfalls]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 20.1.1–20.1.5

### Solution 20.1.1 — Missing colon after `if`
{: #sol-20-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `if` header is missing the trailing `:`, so Python cannot tell where the condition ends and the block begins. Adding the colon fixes the parse error.

```python
temperature = 39
if temperature >= 38:
    print("Fever")
```

[Back to Exercise 20.1.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-1-1) &middot; [`sol_20_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_1_1.py)

</details>

### Solution 20.1.2 — Missing colon after `for`
{: #sol-20-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A `for` loop header must end with `:`. Without it the program will not run; adding the colon resolves it.

```python
distances = [58, 108, 150]
for distance in distances:
    print(distance)
```

[Back to Exercise 20.1.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-1-2) &middot; [`sol_20_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_1_2.py)

</details>

### Solution 20.1.3 — Missing colon after `while`
{: #sol-20-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `while` header needs a colon before its block. Adding `:` lets the countdown loop parse and run.

```python
seconds = 3
while seconds > 0:
    print(seconds)
    seconds = seconds - 1
```

[Back to Exercise 20.1.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-1-3) &middot; [`sol_20_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_1_3.py)

</details>

### Solution 20.1.4 — Missing colon after `def`
{: #sol-20-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A function definition must end with `:` after the parameter list. Adding the colon makes the definition valid.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 5))  # 20
```

[Back to Exercise 20.1.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-1-4) &middot; [`sol_20_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_1_4.py)

</details>

### Solution 20.1.5 — Missing colon after `elif`
{: #sol-20-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

Like `if`, an `elif` header requires a trailing `:`. Adding it lets the three-way branch parse.

```python
score = 55
if score >= 60:
    print("Pass")
elif score >= 50:
    print("Borderline")
else:
    print("Fail")
```

[Back to Exercise 20.1.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-1-5) &middot; [`sol_20_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_1_5.py)

</details>

## Solutions 20.2.1–20.2.5

### Solution 20.2.1 — Body not indented
{: #sol-20-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `print` after the `if` must be indented to form the block. Indenting it by four spaces fixes the `IndentationError`.

```python
member = "Alex"
if member == "Alex":
    print("Welcome back")
```

[Back to Exercise 20.2.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-2-1) &middot; [`sol_20_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_2_1.py)

</details>

### Solution 20.2.2 — Inconsistent indentation in a loop
{: #sol-20-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The final `print` is indented more deeply than the loop body, which Python reads as an unexpected indent. Aligning it at the outer level (after the loop) fixes it.

```python
rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
print(total)  # 35
```

[Back to Exercise 20.2.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-2-2) &middot; [`sol_20_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_2_2.py)

</details>

### Solution 20.2.3 — Function body not indented
{: #sol-20-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `return` statement must be indented inside the function. Indenting it four spaces makes the definition valid.

```python
def square_perimeter(side):
    return 4 * side

print(square_perimeter(6))  # 24
```

[Back to Exercise 20.2.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-2-3) &middot; [`sol_20_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_2_3.py)

</details>

### Solution 20.2.4 — Over-indented statement
{: #sol-20-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The second `print` is indented inconsistently relative to the `if` block, causing an `IndentationError`. Matching the block's indentation (here, dedenting it to the top level) fixes it.

```python
temperature = 100
if temperature >= 100:
    print("Boiling")
print("Done checking")
```

[Back to Exercise 20.2.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-2-4) &middot; [`sol_20_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_2_4.py)

</details>

### Solution 20.2.5 — Indentation mixing two blocks
{: #sol-20-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The closing `print` is indented two spaces, matching neither the loop body nor the top level, so Python raises an `IndentationError`. Dedenting it to the top level fixes it.

```python
grades = [88, 91, 79]
for grade in grades:
    print(grade)
print("Report complete")
```

[Back to Exercise 20.2.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-2-5) &middot; [`sol_20_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_2_5.py)

</details>

## Solutions 20.3.1–20.3.5

### Solution 20.3.1 — Assignment inside an `if`
{: #sol-20-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

`=` assigns and cannot appear as a condition; comparing requires `==`. Using `==` makes the test valid.

```python
thermostat = 20
if thermostat == 20:
    print("Comfortable")
```

[Back to Exercise 20.3.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-3-1) &middot; [`sol_20_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_3_1.py)

</details>

### Solution 20.3.2 — Assignment when comparing a password length
{: #sol-20-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A condition must compare with `==`, not assign with `=`. Switching to `==` fixes the error.

```python
length = 8
if length == 8:
    print("Valid length")
```

[Back to Exercise 20.3.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-3-2) &middot; [`sol_20_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_3_2.py)

</details>

### Solution 20.3.3 — Equality used where assignment is meant
{: #sol-20-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`balance == 100` compares instead of assigning, so `balance` is never created and the `print` raises `NameError`. Use a single `=` to assign.

```python
balance = 100
print(balance)  # 100
```

[Back to Exercise 20.3.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-3-3) &middot; [`sol_20_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_3_3.py)

</details>

### Solution 20.3.4 — Assignment inside a `while`
{: #sol-20-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A `while` condition cannot use `=`; it needs a comparison. The intended loop continues while the count is below 50, so use `<`.

```python
count = 5
while count < 50:
    count = count * 2
    print(count)
```

[Back to Exercise 20.3.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-3-4) &middot; [`sol_20_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_3_4.py)

</details>

### Solution 20.3.5 — Equality used for assignment
{: #sol-20-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`speed == 60` does not create `speed`; the later `print` raises `NameError`. A single `=` assigns the value.

```python
speed = 60
print("Speed:", speed)  # Speed: 60
```

[Back to Exercise 20.3.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-3-5) &middot; [`sol_20_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_3_5.py)

</details>

## Solutions 20.4.1–20.4.5

### Solution 20.4.1 — Printing before assigning
{: #sol-20-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`students` is used on the first line but assigned on the second, raising `NameError`. Assign before using.

```python
students = 30
print(students)
```

[Back to Exercise 20.4.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-4-1) &middot; [`sol_20_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_4_1.py)

</details>

### Solution 20.4.2 — Using a sum before it exists
{: #sol-20-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`total` is printed before it is computed, causing `NameError`. Move the assignment above the `print`.

```python
first = 70
second = 85
total = first + second
print(total)
```

[Back to Exercise 20.4.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-4-2) &middot; [`sol_20_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_4_2.py)

</details>

### Solution 20.4.3 — Using a result before computing it
{: #sol-20-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`area` is referenced before it is assigned, raising `NameError`. Compute `area` first, then print it.

```python
radius = 3
area = 3.14159 * radius * radius
print(area)
```

[Back to Exercise 20.4.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-4-3) &middot; [`sol_20_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_4_3.py)

</details>

### Solution 20.4.4 — Reading a counter that is set later
{: #sol-20-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`laps` is used before it is created, so the `print` raises `NameError`. Assign `laps` before printing it.

```python
laps = 4
print("Laps:", laps)
```

[Back to Exercise 20.4.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-4-4) &middot; [`sol_20_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_4_4.py)

</details>

### Solution 20.4.5 — Using a price before defining it
{: #sol-20-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`price` is multiplied before it is assigned, raising `NameError`. Define `price` before the calculation.

```python
quantity = 3
price = 2
print(quantity * price)
```

[Back to Exercise 20.4.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-4-5) &middot; [`sol_20_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_4_5.py)

</details>

## Solutions 20.5.1–20.5.5

### Solution 20.5.1 — Misspelled variable in a print
{: #sol-20-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`greting` is a different name from `greeting`, so Python raises `NameError`. Use the correct spelling.

```python
greeting = "Good morning"
print(greeting)
```

[Back to Exercise 20.5.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-5-1) &middot; [`sol_20_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_5_1.py)

</details>

### Solution 20.5.2 — Misspelled variable in a calculation
{: #sol-20-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`sped` was never defined; only `speed` exists, so the line raises `NameError`. Fix the spelling.

```python
speed = 60
hours = 2
distance = speed * hours
print(distance)  # 120
```

[Back to Exercise 20.5.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-5-2) &middot; [`sol_20_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_5_2.py)

</details>

### Solution 20.5.3 — Inconsistent capitalization
{: #sol-20-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Python is case-sensitive: `Temperature` and `temperature` are different names, so the `print` raises `NameError`. Match the case used at assignment.

```python
Temperature = 31
print(Temperature)
```

[Back to Exercise 20.5.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-5-3) &middot; [`sol_20_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_5_3.py)

</details>

### Solution 20.5.4 — Misspelled variable when updating
{: #sol-20-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`bil` is a misspelling of `bill`, so the calculation raises `NameError`. Use the correct name.

```python
bill = 40
tip = 6
total = bill + tip
print(total)  # 46
```

[Back to Exercise 20.5.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-5-4) &middot; [`sol_20_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_5_4.py)

</details>

### Solution 20.5.5 — Misspelled list name
{: #sol-20-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`score` (singular) was never defined; the list is named `scores`, so `sum(score)` raises `NameError`. Pass the correct list name.

```python
scores = [80, 90, 100]
average = sum(scores) / len(scores)
print(average)  # 90.0
```

[Back to Exercise 20.5.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-5-5) &middot; [`sol_20_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_5_5.py)

</details>

## Solutions 20.6.1–20.6.5

### Solution 20.6.1 — Joining text and a number
{: #sol-20-6-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

You cannot add a string to an integer; `"Steps today: " + steps` raises `TypeError`. Convert the number with `str()`.

```python
steps = 8000
print("Steps today: " + str(steps))
```

[Back to Exercise 20.6.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-6-1) &middot; [`sol_20_6_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_6_1.py)

</details>

### Solution 20.6.2 — Adding a number to a string label
{: #sol-20-6-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Mixing `str` and `int` with `+` raises `TypeError`. Convert `liters` to a string before concatenating.

```python
liters = 2
print("Drink " + str(liters) + " liters")
```

[Back to Exercise 20.6.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-6-2) &middot; [`sol_20_6_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_6_2.py)

</details>

### Solution 20.6.3 — Concatenating a price into a message
{: #sol-20-6-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`"...$" + price` adds a string and an int, raising `TypeError`. Wrap `price` in `str()`.

```python
price = 15
message = "Ticket costs $" + str(price)
print(message)
```

[Back to Exercise 20.6.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-6-3) &middot; [`sol_20_6_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_6_3.py)

</details>

### Solution 20.6.4 — Combining a count with text
{: #sol-20-6-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`books + " books..."` adds an int to a string, raising `TypeError`. Convert `books` to a string first.

```python
books = 12
print(str(books) + " books on the shelf")
```

[Back to Exercise 20.6.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-6-4) &middot; [`sol_20_6_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_6_4.py)

</details>

### Solution 20.6.5 — Treating a string as a number
{: #sol-20-6-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime/Logical

`score` holds the text `"75"`, so `score + 10` mixes a string and an int and raises `TypeError`. Convert `score` to an integer (or store it as one) before adding.

```python
score = int("75")
print(score + 10)
```

[Back to Exercise 20.6.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-6-5) &middot; [`sol_20_6_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_6_5.py)

</details>

## Solutions 20.7.1–20.7.5

### Solution 20.7.1 — Adding to raw input
{: #sol-20-7-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`input()` returns text, so `year + 1` adds a string and an int, raising `TypeError`. Wrap the input in `int()`.

```python
year = int(input("Enter the year: "))
print(year + 1)
```

[Back to Exercise 20.7.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-7-1) &middot; [`sol_20_7_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_7_1.py)

</details>

### Solution 20.7.2 — Doubling a typed quantity
{: #sol-20-7-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`cookies` is text, so `cookies * 2` repeats the string (e.g. `"1212"`) instead of doubling the number. Convert the input to `int` first.

```python
cookies = int(input("How many cookies? "))
print(cookies * 2 == 24)  # for input 12
```

[Back to Exercise 20.7.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-7-2) &middot; [`sol_20_7_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_7_2.py)

</details>

### Solution 20.7.3 — Summing two typed numbers
{: #sol-20-7-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`second` is left as text, so `first + second` adds an int and a string, raising `TypeError`. Convert `second` with `int()` as well.

```python
first = int(input("First price: "))
second = int(input("Second price: "))
print(first + second)
```

[Back to Exercise 20.7.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-7-3) &middot; [`sol_20_7_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_7_3.py)

</details>

### Solution 20.7.4 — Comparing typed age to a limit
{: #sol-20-7-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`age` is a string, so `age >= 18` compares a string with an int and raises `TypeError`. Convert the input to `int` before comparing.

```python
age = int(input("Your age: "))
if age >= 18:
    print("Adult")
```

[Back to Exercise 20.7.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-7-4) &middot; [`sol_20_7_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_7_4.py)

</details>

### Solution 20.7.5 — Averaging a typed temperature
{: #sol-20-7-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`temperature` is text, so `temperature / 2` raises `TypeError`. Convert the input to a number first (`float` allows decimals).

```python
temperature = float(input("Temperature: "))
print(temperature / 2)
```

[Back to Exercise 20.7.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-7-5) &middot; [`sol_20_7_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_7_5.py)

</details>

## Solutions 20.8.1–20.8.5

### Solution 20.8.1 — Splitting students into teams
{: #sol-20-8-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`/` gives `7.5`, but full teams need integer division. Use `//` to get `7`.

```python
students = 30
team_size = 4
print(students // team_size)  # 7
```

[Back to Exercise 20.8.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-8-1) &middot; [`sol_20_8_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_8_1.py)

</details>

### Solution 20.8.2 — Pages per chapter
{: #sol-20-8-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`52 / 5` is `10.4`; the program wants whole pages. Use `//` for the integer quotient `10`.

```python
pages = 52
chapters = 5
print(pages // chapters)  # 10
```

[Back to Exercise 20.8.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-8-2) &middot; [`sol_20_8_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_8_2.py)

</details>

### Solution 20.8.3 — Counting full boxes
{: #sol-20-8-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`40 / 6` is `6.66...`, but you can only fill whole boxes. `//` gives the correct `6`.

```python
eggs = 40
per_box = 6
full_boxes = eggs // per_box
print(full_boxes)  # 6
```

[Back to Exercise 20.8.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-8-3) &middot; [`sol_20_8_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_8_3.py)

</details>

### Solution 20.8.4 — Whole minutes from seconds
{: #sol-20-8-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`200 / 60` is `3.33...`; whole minutes need `//`, giving `3`.

```python
seconds = 200
minutes = seconds // 60
print(minutes)  # 3
```

[Back to Exercise 20.8.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-8-4) &middot; [`sol_20_8_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_8_4.py)

</details>

### Solution 20.8.5 — Sharing marbles evenly
{: #sol-20-8-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`25 / 3` is `8.33...`; each child gets a whole number of marbles. `//` yields `8`.

```python
marbles = 25
children = 3
print(marbles // children)  # 8
```

[Back to Exercise 20.8.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-8-5) &middot; [`sol_20_8_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_8_5.py)

</details>

## Solutions 20.9.1–20.9.5

### Solution 20.9.1 — Area of a square
{: #sol-20-9-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`^` is bitwise XOR, not exponent, so `5 ^ 2` is `7`, not `25`. Use `**` for powers.

```python
side = 5
print(side ** 2)  # 25
```

[Back to Exercise 20.9.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-9-1) &middot; [`sol_20_9_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_9_1.py)

</details>

### Solution 20.9.2 — Cube of a number
{: #sol-20-9-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`4 ^ 3` computes XOR (`7`), not `4` cubed. Use `**`.

```python
base = 4
print(base ** 3)  # 64
```

[Back to Exercise 20.9.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-9-2) &middot; [`sol_20_9_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_9_2.py)

</details>

### Solution 20.9.3 — Compound growth
{: #sol-20-9-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`2 ^ 10` is XOR (`8`), not `2` to the tenth. Use `**` for exponentiation.

```python
print(2 ** 10)  # 1024
```

[Back to Exercise 20.9.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-9-3) &middot; [`sol_20_9_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_9_3.py)

</details>

### Solution 20.9.4 — Volume of a cube
{: #sol-20-9-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`3 ^ 3` is XOR (`0`), not `3` cubed. Use `**` to raise to a power.

```python
edge = 3
volume = edge ** 3
print(volume)  # 27
```

[Back to Exercise 20.9.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-9-4) &middot; [`sol_20_9_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_9_4.py)

</details>

### Solution 20.9.5 — Energy term squared
{: #sol-20-9-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`6 ^ 2` is XOR (`4`), not `6` squared. Use `**`.

```python
speed = 6
print(speed ** 2)  # 36
```

[Back to Exercise 20.9.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-9-5) &middot; [`sol_20_9_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_9_5.py)

</details>

## Solutions 20.10.1–20.10.5

### Solution 20.10.1 — Setting a fourth temperature
{: #sol-20-10-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`readings` has indexes 0–2, so assigning to `readings[3]` raises `IndexError`; assignment cannot grow a list. Use `append` to add a fourth value.

```python
readings = [20, 22, 21]
readings.append(23)
print(readings)
```

[Back to Exercise 20.10.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-10-1) &middot; [`sol_20_10_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_10_1.py)

</details>

### Solution 20.10.2 — Recording a new score
{: #sol-20-10-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`scores[3]` does not exist yet, so assigning to it raises `IndexError`. Use `append` to add the new score.

```python
scores = [10, 15, 20]
scores.append(25)
print(scores)
```

[Back to Exercise 20.10.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-10-2) &middot; [`sol_20_10_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_10_2.py)

</details>

### Solution 20.10.3 — Filling in a weekly total
{: #sol-20-10-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Index 3 is past the end of a three-item list, so the assignment raises `IndexError`. Use `append` to extend the list.

```python
weekly_sales = [100, 120, 90]
weekly_sales.append(110)
print(weekly_sales)
```

[Back to Exercise 20.10.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-10-3) &middot; [`sol_20_10_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_10_3.py)

</details>

### Solution 20.10.4 — Adding a fourth runner's time
{: #sol-20-10-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(lap_times)` is `3`, which is one past the last valid index, so the assignment raises `IndexError`. Use `append`.

```python
lap_times = [45, 47, 44]
lap_times.append(46)
print(lap_times)
```

[Back to Exercise 20.10.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-10-4) &middot; [`sol_20_10_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_10_4.py)

</details>

### Solution 20.10.5 — Appending a measurement
{: #sol-20-10-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Assigning to `ph_values[3]` on a three-item list raises `IndexError`. Use `append` to add a new reading.

```python
ph_values = [7.0, 6.8, 7.2]
ph_values.append(6.9)
print(ph_values)
```

[Back to Exercise 20.10.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-10-5) &middot; [`sol_20_10_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_10_5.py)

</details>

## Solutions 20.11.1–20.11.5

### Solution 20.11.1 — Reading the last color
{: #sol-20-11-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Indexes run 0–2, so `colors[3]` is out of range and raises `IndexError`. The last item is at index `2`.

```python
colors = ["red", "green", "blue"]
print(colors[2])
```

[Back to Exercise 20.11.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-11-1) &middot; [`sol_20_11_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_11_1.py)

</details>

### Solution 20.11.2 — Printing each day's high
{: #sol-20-11-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`range(5)` reaches index 4, but the list has only indexes 0–3, so the loop raises `IndexError`. Loop to `len(highs)` (or iterate the list directly).

```python
highs = [28, 30, 29, 31]
for i in range(len(highs)):
    print(highs[i])
```

[Back to Exercise 20.11.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-11-2) &middot; [`sol_20_11_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_11_2.py)

</details>

### Solution 20.11.3 — Showing the third prize
{: #sol-20-11-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The list has only two items (indexes 0 and 1), so `prizes[2]` raises `IndexError`. To print a third prize, the list must contain one.

```python
prizes = ["gold", "silver", "bronze"]
print(prizes[2])
```

[Back to Exercise 20.11.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-11-3) &middot; [`sol_20_11_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_11_3.py)

</details>

### Solution 20.11.4 — Last item by length
{: #sol-20-11-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(students)` is `3`, one past the last index, so `students[3]` raises `IndexError`. The last index is `len(students) - 1`.

```python
students = ["Mia", "Noah", "Liam"]
print(students[len(students) - 1])
```

[Back to Exercise 20.11.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-11-4) &middot; [`sol_20_11_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_11_4.py)

</details>

### Solution 20.11.5 — Looping one step too far
{: #sol-20-11-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`index <= len(prices)` lets `index` reach `3`, which is out of range, so the loop raises `IndexError`. Stop with `<` instead of `<=`.

```python
prices = [3, 5, 9]
index = 0
while index < len(prices):
    print(prices[index])
    index = index + 1
```

[Back to Exercise 20.11.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-11-5) &middot; [`sol_20_11_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_11_5.py)

</details>

## Solutions 20.12.1–20.12.5

### Solution 20.12.1 — Building a shopping list
{: #sol-20-12-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Parentheses create a tuple, which has no `append` method, so the call raises `AttributeError`. Use square brackets to make a list.

```python
groceries = ["milk", "bread", "eggs"]
groceries.append("butter")
print(groceries)
```

[Back to Exercise 20.12.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-12-1) &middot; [`sol_20_12_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_12_1.py)

</details>

### Solution 20.12.2 — Collecting daily steps
{: #sol-20-12-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`steps` is a tuple, so `append` raises `AttributeError`. Use brackets to create a list.

```python
steps = [8000, 9500, 7000]
steps.append(10000)
print(steps)
```

[Back to Exercise 20.12.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-12-2) &middot; [`sol_20_12_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_12_2.py)

</details>

### Solution 20.12.3 — A list of temperatures
{: #sol-20-12-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Parentheses make a tuple, which is immutable, so `temperatures[0] = 19` raises `TypeError`. Use brackets to make an editable list.

```python
temperatures = [21, 22, 20]
temperatures[0] = 19
print(temperatures)
```

[Back to Exercise 20.12.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-12-3) &middot; [`sol_20_12_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_12_3.py)

</details>

### Solution 20.12.4 — Listing class names
{: #sol-20-12-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`subjects` is a tuple, so `append` raises `AttributeError`. Use square brackets for a list.

```python
subjects = ["Math", "Science"]
subjects.append("History")
print(subjects)
```

[Back to Exercise 20.12.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-12-4) &middot; [`sol_20_12_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_12_4.py)

</details>

### Solution 20.12.5 — A list of scores to extend
{: #sol-20-12-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Parentheses create a tuple, which has no `append`, raising `AttributeError`. Use brackets to make a list.

```python
scores = [88, 92]
scores.append(75)
print(scores)
```

[Back to Exercise 20.12.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-12-5) &middot; [`sol_20_12_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_12_5.py)

</details>

## Solutions 20.13.1–20.13.5

### Solution 20.13.1 — Capitalizing a name
{: #sol-20-13-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Strings are immutable, so `name[0] = "S"` raises `TypeError`. Build a new string instead.

```python
name = "sam"
name = "S" + name[1:]
print(name)
```

[Back to Exercise 20.13.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-13-1) &middot; [`sol_20_13_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_13_1.py)

</details>

### Solution 20.13.2 — Fixing a typo in a word
{: #sol-20-13-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

You cannot assign to a single character of a string; `word[1] = "e"` raises `TypeError`. Rebuild the word from slices.

```python
word = "hpllo"
word = word[0] + "e" + word[2:]
print(word)
```

[Back to Exercise 20.13.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-13-2) &middot; [`sol_20_13_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_13_2.py)

</details>

### Solution 20.13.3 — Replacing a digit in a code
{: #sol-20-13-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Strings are immutable, so `code[0] = "9"` raises `TypeError`. Construct a new string.

```python
code = "12345"
code = "9" + code[1:]
print(code)
```

[Back to Exercise 20.13.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-13-3) &middot; [`sol_20_13_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_13_3.py)

</details>

### Solution 20.13.4 — Masking a letter
{: #sol-20-13-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Assigning to `secret[3]` fails because strings cannot be changed in place, raising `TypeError`. Rebuild the string from its slices.

```python
secret = "open"
secret = secret[:3] + "*"
print(secret)
```

[Back to Exercise 20.13.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-13-4) &middot; [`sol_20_13_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_13_4.py)

</details>

### Solution 20.13.5 — Correcting a unit label
{: #sol-20-13-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`unit[0] = "K"` tries to mutate an immutable string, raising `TypeError`. Make a new string instead.

```python
unit = "km"
unit = "K" + unit[1:]
print(unit)
```

[Back to Exercise 20.13.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-13-5) &middot; [`sol_20_13_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_13_5.py)

</details>

## Solutions 20.14.1–20.14.5

### Solution 20.14.1 — Checking a student's full name
{: #sol-20-14-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The name built with `join` is a brand-new string object, so `is` (which tests identity) returns `False` even though the text matches. Compare values with `==`.

```python
enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name == enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
```

[Back to Exercise 20.14.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-14-1) &middot; [`sol_20_14_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_14_1.py)

</details>

### Solution 20.14.2 — Matching a password phrase
{: #sol-20-14-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The built string is a different object from the stored literal, so `is` returns `False` even though the text matches. Compare values with `==`.

```python
stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase == stored_phrase:
    print("Access granted")
else:
    print("Access denied")
```

[Back to Exercise 20.14.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-14-2) &middot; [`sol_20_14_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_14_2.py)

</details>

### Solution 20.14.3 — Confirming a recipe title
{: #sol-20-14-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The title built by concatenation is a separate string object, so `is` returns `False` even when the text is identical. Use `==` to compare the values.

```python
saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title == saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
```

[Back to Exercise 20.14.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-14-3) &middot; [`sol_20_14_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_14_3.py)

</details>

### Solution 20.14.4 — Comparing two shopping lists
{: #sol-20-14-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Two lists with identical contents are still distinct objects, so `is` is always `False` here. Use `==` to compare contents.

```python
cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one == cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
```

[Back to Exercise 20.14.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-14-4) &middot; [`sol_20_14_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_14_4.py)

</details>

### Solution 20.14.5 — Verifying a reading list
{: #sol-20-14-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Two lists with identical contents are still different objects, so `is` is always `False` here. Use `==` to compare contents.

```python
planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far == planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
```

[Back to Exercise 20.14.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-14-5) &middot; [`sol_20_14_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_14_5.py)

</details>

## Solutions 20.15.1–20.15.5

### Solution 20.15.1 — Reading the current temperature
{: #sol-20-15-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Writing `current_temperature` without parentheses prints the function object instead of calling it. Add `()` to invoke it.

```python
def current_temperature():
    return 21.5

print("Temperature:", current_temperature())
```

[Back to Exercise 20.15.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-15-1) &middot; [`sol_20_15_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_15_1.py)

</details>

### Solution 20.15.2 — Counting words in a sentence
{: #sol-20-15-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`word_count` alone is the function object; it was never called with the sentence. Call it as `word_count(note)`.

```python
def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count(note))
```

[Back to Exercise 20.15.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-15-2) &middot; [`sol_20_15_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_15_2.py)

</details>

### Solution 20.15.3 — Rolling for a starting number
{: #sol-20-15-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`score = starting_score` stores the function itself, not its result. Add `()` to call it.

```python
def starting_score():
    return 100

score = starting_score()
print("You begin with", score, "points")
```

[Back to Exercise 20.15.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-15-3) &middot; [`sol_20_15_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_15_3.py)

</details>

### Solution 20.15.4 — Area of a circle
{: #sol-20-15-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`circle_area / 2` tries to divide the function object by 2, raising `TypeError`. Call the function first, then divide its result.

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area(4) / 2)
```

[Back to Exercise 20.15.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-15-4) &middot; [`sol_20_15_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_15_4.py)

</details>

### Solution 20.15.5 — Greeting the next runner
{: #sol-20-15-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`message = greet_runner` stores the function, so the print shows a function object. Call it with an argument.

```python
def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner("Sam")
print(message)
```

[Back to Exercise 20.15.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-15-5) &middot; [`sol_20_15_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_15_5.py)

</details>

## Solutions 20.16.1–20.16.5

### Solution 20.16.1 — Converting miles to kilometers
{: #sol-20-16-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function computes `km` but never returns it, so the call yields `None`. Add a `return`.

```python
def miles_to_km(miles):
    km = miles * 1.60934
    return km

print("Kilometers:", miles_to_km(5))
```

[Back to Exercise 20.16.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-16-1) &middot; [`sol_20_16_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_16_1.py)

</details>

### Solution 20.16.2 — Averaging three test grades
{: #sol-20-16-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The average is computed into `average_value` but never returned, so `None` is printed. Return the value.

```python
def average(a, b, c):
    total = a + b + c
    average_value = total / 3
    return average_value

print("Average:", average(80, 90, 100))
```

[Back to Exercise 20.16.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-16-2) &middot; [`sol_20_16_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_16_2.py)

</details>

### Solution 20.16.3 — Doubling a recipe
{: #sol-20-16-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`doubled` is computed but not returned, so `flour` becomes `None`. Add `return doubled`.

```python
def double_amount(cups):
    doubled = cups * 2
    return doubled

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
```

[Back to Exercise 20.16.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-16-3) &middot; [`sol_20_16_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_16_3.py)

</details>

### Solution 20.16.4 — Perimeter of a rectangle
{: #sol-20-16-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The perimeter `p` is calculated but never returned, so the program prints `None`. Return `p`.

```python
def perimeter(length, width):
    p = 2 * (length + width)
    return p

print("Perimeter:", perimeter(6, 4))
```

[Back to Exercise 20.16.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-16-4) &middot; [`sol_20_16_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_16_4.py)

</details>

### Solution 20.16.5 — Tax on a purchase
{: #sol-20-16-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The tax is computed into `tax` but never returned, so the result is `None`. Add a `return`.

```python
def tax_owed(price, rate):
    tax = price * rate / 100
    return tax

print("Tax:", tax_owed(200, 8))
```

[Back to Exercise 20.16.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-16-5) &middot; [`sol_20_16_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_16_5.py)

</details>

## Solutions 20.17.1–20.17.5

### Solution 20.17.1 — Tallying rainfall
{: #sol-20-17-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Assigning to `total_rain` inside the function makes it local, so reading it on the right raises `UnboundLocalError`. Declare it `global`.

```python
total_rain = 0.0

def add_rain(today):
    global total_rain
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
```

[Back to Exercise 20.17.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-17-1) &middot; [`sol_20_17_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_17_1.py)

</details>

### Solution 20.17.2 — Keeping a running balance
{: #sol-20-17-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function assigns to `balance`, so Python treats it as local and the read raises `UnboundLocalError`. Add `global balance`.

```python
balance = 500

def withdraw(amount):
    global balance
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
```

[Back to Exercise 20.17.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-17-2) &middot; [`sol_20_17_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_17_2.py)

</details>

### Solution 20.17.3 — Counting visitors
{: #sol-20-17-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Because `visitors` is assigned inside `enter`, Python marks it local and raises `UnboundLocalError`. Declare it `global`.

```python
visitors = 0

def enter():
    global visitors
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
```

[Back to Exercise 20.17.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-17-3) &middot; [`sol_20_17_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_17_3.py)

</details>

### Solution 20.17.4 — Accumulating distance
{: #sol-20-17-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Assigning `distance_km` inside `drive` makes it local, so the read raises `UnboundLocalError`. Add `global distance_km`.

```python
distance_km = 0

def drive(leg):
    global distance_km
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
```

[Back to Exercise 20.17.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-17-4) &middot; [`sol_20_17_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_17_4.py)

</details>

### Solution 20.17.5 — Building a points streak
{: #sol-20-17-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`streak` is assigned inside the function, so Python treats it as local and raises `UnboundLocalError`. Declare it `global`.

```python
streak = 1

def double_streak():
    global streak
    streak = streak * 2

double_streak()
print("Streak:", streak)
```

[Back to Exercise 20.17.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-17-5) &middot; [`sol_20_17_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_17_5.py)

</details>

## Solutions 20.18.1–20.18.5

### Solution 20.18.1 — Saving a shopping list
{: #sol-20-18-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The file is opened but never closed, so the handle leaks and buffered data may not flush. Use a `with` block, which closes automatically.

```python
groceries = "milk\neggs\nbread\n"
with open("groceries.txt", "w") as list_file:
    list_file.write(groceries)
print("Shopping list saved")
```

[Back to Exercise 20.18.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-18-1) &middot; [`sol_20_18_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_18_1.py)

</details>

### Solution 20.18.2 — Logging a temperature reading
{: #sol-20-18-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The file handle is never closed. Wrap the write in a `with` block so the file is closed safely.

```python
with open("temps.txt", "a") as log:
    log.write("21.5\n")
```

[Back to Exercise 20.18.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-18-2) &middot; [`sol_20_18_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_18_2.py)

</details>

### Solution 20.18.3 — Recording a high score
{: #sol-20-18-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`score_file` is opened but never closed. Use `with open(...)` so the file closes automatically after writing.

```python
high_score = 4200
with open("highscore.txt", "w") as score_file:
    score_file.write(str(high_score))
print("High score recorded")
```

[Back to Exercise 20.18.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-18-3) &middot; [`sol_20_18_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_18_3.py)

</details>

### Solution 20.18.4 — Writing a daily journal entry
{: #sol-20-18-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The file is left open. A `with` block guarantees the file is closed even if an error occurs.

```python
entry = "Today I walked 10000 steps.\n"
with open("journal.txt", "w") as journal:
    journal.write(entry)
print("Entry written")
```

[Back to Exercise 20.18.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-18-4) &middot; [`sol_20_18_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_18_4.py)

</details>

### Solution 20.18.5 — Storing a measured weight
{: #sol-20-18-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`weight_file` is never closed, risking unflushed data. Use a `with` block to close it safely.

```python
weight_kg = 72.4
with open("weight.txt", "w") as weight_file:
    weight_file.write(f"{weight_kg}\n")
```

[Back to Exercise 20.18.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-18-5) &middot; [`sol_20_18_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_18_5.py)

</details>

## Solutions 20.19.1–20.19.5

### Solution 20.19.1 — Converting a typed age
{: #sol-20-19-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The bare `except:` hides every error, including programming mistakes. Catch only `ValueError`, which is the error `int()` raises on bad text.

```python
text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a whole number")
```

[Back to Exercise 20.19.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-19-1) &middot; [`sol_20_19_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_19_1.py)

</details>

### Solution 20.19.2 — Dividing a bill among friends
{: #sol-20-19-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A broad `except:` would swallow unrelated bugs. Catch the specific `ZeroDivisionError` that division by zero raises.

```python
bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("There must be at least one person")
```

[Back to Exercise 20.19.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-19-2) &middot; [`sol_20_19_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_19_2.py)

</details>

### Solution 20.19.3 — Looking up a price
{: #sol-20-19-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The bare `except:` hides all errors. A missing dictionary key raises `KeyError`, so catch exactly that.

```python
prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except KeyError:
    print("That item is not on the price list")
```

[Back to Exercise 20.19.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-19-3) &middot; [`sol_20_19_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_19_3.py)

</details>

### Solution 20.19.4 — Parsing a temperature
{: #sol-20-19-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A bare `except:` masks unrelated problems. `float()` raises `ValueError` on non-numeric text, so catch `ValueError`.

```python
reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except ValueError:
    print("That is not a valid temperature")
```

[Back to Exercise 20.19.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-19-4) &middot; [`sol_20_19_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_19_4.py)

</details>

### Solution 20.19.5 — Reading a list position
{: #sol-20-19-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The broad `except:` hides real bugs. An out-of-range index raises `IndexError`, so catch exactly that.

```python
scores = [88, 92]
try:
    print("Third score:", scores[2])
except IndexError:
    print("There is no score at that position")
```

[Back to Exercise 20.19.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-19-5) &middot; [`sol_20_19_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_19_5.py)

</details>

## Solutions 20.20.1–20.20.5

### Solution 20.20.1 — Accepting a yes answer
{: #sol-20-20-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`"YES" == "yes"` is `False` because case differs. Normalize the case first with `.lower()`.

```python
answer = "YES"
if answer.lower() == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
```

[Back to Exercise 20.20.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-20-1) &middot; [`sol_20_20_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_20_1.py)

</details>

### Solution 20.20.2 — Matching a chosen color
{: #sol-20-20-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`favorite.upper()` gives `"BLUE"`, which never equals the lowercase `"blue"`. Normalize both sides to the same case, for example `.lower() == "blue"`.

```python
favorite = "Blue"
if favorite.lower() == "blue":
    print("You picked blue")
```

[Back to Exercise 20.20.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-20-2) &middot; [`sol_20_20_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_20_2.py)

</details>

### Solution 20.20.3 — Checking a chemical symbol
{: #sol-20-20-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`"NA" == "Na"` is `False` because the cases differ. Normalize the typed symbol, for example with `.capitalize()`.

```python
symbol = "NA"
if symbol.capitalize() == "Na":
    print("That is sodium")
```

[Back to Exercise 20.20.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-20-3) &middot; [`sol_20_20_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_20_3.py)

</details>

### Solution 20.20.4 — Looking up a city name
{: #sol-20-20-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The list stores `"Paris"`, so a lowercase `"paris"` is not found. Compare in a consistent case, for example by lowercasing each city.

```python
cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in [city.lower() for city in cities]:
    print("City found")
else:
    print("City not found")
```

[Back to Exercise 20.20.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-20-4) &middot; [`sol_20_20_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_20_4.py)

</details>

### Solution 20.20.5 — Confirming a unit
{: #sol-20-20-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`unit.upper()` produces `"KG"`, which never equals lowercase `"kg"`. Compare against the same case you converted to, for example `.lower() == "kg"`.

```python
unit = "KG"
if unit.lower() == "kg":
    print("Kilograms")
```

[Back to Exercise 20.20.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-20-5) &middot; [`sol_20_20_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_20_5.py)

</details>

## Solutions 20.21.1–20.21.5

### Solution 20.21.1 — Printing each planet
{: #sol-20-21-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The loop indexes with `i` but prints `planet`, which was never defined, raising `NameError`. Iterate over the items directly.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
for planet in planets:
    print(planet)
```

[Back to Exercise 20.21.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-21-1) &middot; [`sol_20_21_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_21_1.py)

</details>

### Solution 20.21.2 — Summing daily sales
{: #sol-20-21-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`total + sales` adds an integer to the whole list, raising `TypeError`. Iterate over the items and add each value.

```python
sales = [120, 85, 200, 95]
total = 0
for amount in sales:
    total = total + amount
print("Total sales:", total)
```

[Back to Exercise 20.21.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-21-2) &middot; [`sol_20_21_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_21_2.py)

</details>

### Solution 20.21.3 — Greeting each guest
{: #sol-20-21-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range(len(guests))` yields the numbers 0, 1, 2, so the greeting prints numbers, not names. Iterate over the guests directly.

```python
guests = ["Ana", "Ben", "Cara"]
for guest in guests:
    print("Welcome,", guest)
```

[Back to Exercise 20.21.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-21-3) &middot; [`sol_20_21_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_21_3.py)

</details>

### Solution 20.21.4 — Doubling each measurement
{: #sol-20-21-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range(len(...))` makes `m` the index 0, 1, 2, so it doubles indexes, not values. Iterate over the measurements directly.

```python
measurements = [3, 5, 8]
for m in measurements:
    print(m * 2)
```

[Back to Exercise 20.21.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-21-4) &middot; [`sol_20_21_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_21_4.py)

</details>

### Solution 20.21.5 — Listing the ingredients
{: #sol-20-21-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`item` becomes the index 0, 1, 2 instead of the ingredient name. Iterate over the list itself.

```python
ingredients = ["flour", "sugar", "butter"]
for item in ingredients:
    print(item)
```

[Back to Exercise 20.21.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-21-5) &middot; [`sol_20_21_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_21_5.py)

</details>

## Solutions 20.22.1–20.22.5

### Solution 20.22.1 — Counting items in a basket
{: #sol-20-22-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Assigning `len = [4, 8, 15]` shadows the built-in `len`, so `len(fruit)` tries to call a list and raises `TypeError`. Rename the variable.

```python
basket = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
```

[Back to Exercise 20.22.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-22-1) &middot; [`sol_20_22_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_22_1.py)

</details>

### Solution 20.22.2 — Totaling a receipt
{: #sol-20-22-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`sum = 0` shadows the built-in `sum`, so `sum(prices)` tries to call an integer and raises `TypeError`. Use a different variable name.

```python
running_total = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
```

[Back to Exercise 20.22.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-22-2) &middot; [`sol_20_22_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_22_2.py)

</details>

### Solution 20.22.3 — Turning a word into letters
{: #sol-20-22-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`list = "abc"` shadows the built-in `list`, so `list("hello")` tries to call a string and raises `TypeError`. Rename the variable.

```python
word = "abc"
letters = list("hello")
print(letters)
```

[Back to Exercise 20.22.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-22-3) &middot; [`sol_20_22_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_22_3.py)

</details>

### Solution 20.22.4 — Labeling a measurement
{: #sol-20-22-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`str = "kilograms"` shadows the built-in `str`, so `str(weight)` tries to call a string and raises `TypeError`. Rename the variable.

```python
unit = "kilograms"
weight = 70
print(str(weight) + " " + unit)
```

[Back to Exercise 20.22.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-22-4) &middot; [`sol_20_22_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_22_4.py)

</details>

### Solution 20.22.5 — Finding the largest reading
{: #sol-20-22-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`max = 9999` shadows the built-in `max`, so `max(readings)` tries to call an integer and raises `TypeError`. Use a different name.

```python
ceiling = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
```

[Back to Exercise 20.22.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-22-5) &middot; [`sol_20_22_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_22_5.py)

</details>

## Solutions 20.23.1–20.23.5

### Solution 20.23.1 — Splitting a bill exactly
{: #sol-20-23-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`0.10 + 0.10 + 0.10` is not exactly `0.30` in binary floating-point, so the equality fails. Compare with a small tolerance using `round` or `math.isclose`.

```python
import math

share = 0.10
total = share + share + share
if math.isclose(total, 0.30):
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
```

[Back to Exercise 20.23.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-23-1) &middot; [`sol_20_23_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_23_1.py)

</details>

### Solution 20.23.2 — Adding two distances
{: #sol-20-23-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`0.1 + 0.2` is slightly more than `0.3` in floating-point, so the exact comparison is `False`. Use `math.isclose` to compare with tolerance.

```python
import math

leg_one = 0.1
leg_two = 0.2
if math.isclose(leg_one + leg_two, 0.3):
    print("Distances match")
else:
    print("Distances do not match")
```

[Back to Exercise 20.23.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-23-2) &middot; [`sol_20_23_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_23_2.py)

</details>

### Solution 20.23.3 — Checking a measured volume
{: #sol-20-23-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`0.1 * 3` does not equal `0.3` exactly in floating-point. Compare with a tolerance, for example `math.isclose`.

```python
import math

pour = 0.1
filled = pour * 3
if math.isclose(filled, 0.3):
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
```

[Back to Exercise 20.23.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-23-3) &middot; [`sol_20_23_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_23_3.py)

</details>

### Solution 20.23.4 — Verifying a percentage
{: #sol-20-23-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`0.7 + 0.1` is not exactly `0.8` in binary floating-point, so the strict equality fails. Use `math.isclose` to allow for rounding error.

```python
import math

part_one = 0.7
part_two = 0.1
if math.isclose(part_one + part_two, 0.8):
    print("Percentages add correctly")
else:
    print("Percentages do not add correctly")
```

[Back to Exercise 20.23.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-23-4) &middot; [`sol_20_23_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_23_4.py)

</details>

### Solution 20.23.5 — Comparing a savings target
{: #sol-20-23-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`1.10 * 3` does not land exactly on `3.30` in floating-point. Compare with a tolerance using `math.isclose`.

```python
import math

weekly = 1.10
saved = weekly * 3
if math.isclose(saved, 3.30):
    print("You reached the target")
else:
    print("You did not reach the target")
```

[Back to Exercise 20.23.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-23-5) &middot; [`sol_20_23_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_23_5.py)

</details>

## Solutions 20.24.1–20.24.5

### Solution 20.24.1 — Average speed of a trip
{: #sol-20-24-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The formula is reversed: speed is distance divided by time, not time divided by distance. Swap the operands.

```python
def average_speed(distance, time):
    return distance / time

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
```

[Back to Exercise 20.24.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-24-1) &middot; [`sol_20_24_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_24_1.py)

</details>

### Solution 20.24.2 — Final price after discount
{: #sol-20-24-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A percentage must be divided by 100 first; `price * 20` computes a huge discount. Divide the percent by 100 (or test the discount step alone to catch this).

```python
def final_price(price, percent_off):
    discount = price * percent_off / 100
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
```

[Back to Exercise 20.24.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-24-2) &middot; [`sol_20_24_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_24_2.py)

</details>

### Solution 20.24.3 — Kinetic energy of a moving cart
{: #sol-20-24-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The speed must be squared (`speed ** 2`), but the code multiplies by 2 instead. Testing the squaring step alone would reveal this.

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed ** 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
```

[Back to Exercise 20.24.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-24-3) &middot; [`sol_20_24_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_24_3.py)

</details>

### Solution 20.24.4 — Celsius to Fahrenheit
{: #sol-20-24-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The formula adds 32, but the code subtracts it. Change `- 32` to `+ 32`.

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
```

[Back to Exercise 20.24.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-24-4) &middot; [`sol_20_24_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_24_4.py)

</details>

### Solution 20.24.5 — Average of a list of grades
{: #sol-20-24-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The stray `- 1` skews the average. Testing the bare `sum / len` step alone would expose it; remove the `- 1`.

```python
def average(grades):
    return sum(grades) / len(grades)

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
```

[Back to Exercise 20.24.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-24-5) &middot; [`sol_20_24_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_24_5.py)

</details>

## Solutions 20.25.1–20.25.5

### Solution 20.25.1 — Copying a seating chart
{: #sol-20-25-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`original.copy()` is a shallow copy: the inner row lists are still shared, so appending through `backup` also changes `original`. Use `copy.deepcopy`.

```python
import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = copy.deepcopy(original)
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
```

[Back to Exercise 20.25.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-25-1) &middot; [`sol_20_25_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_25_1.py)

</details>

### Solution 20.25.2 — Backing up monthly budgets
{: #sol-20-25-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Slicing with `[:]` copies only the outer list; the nested lists stay shared, so editing `saved` edits `budgets`. Use `copy.deepcopy`.

```python
import copy

budgets = [[100, 200], [300, 400]]
saved = copy.deepcopy(budgets)
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
```

[Back to Exercise 20.25.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-25-2) &middot; [`sol_20_25_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_25_2.py)

</details>

### Solution 20.25.3 — Duplicating a tic-tac-toe board
{: #sol-20-25-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`list(board)` makes a shallow copy whose inner rows are shared, so editing `trial` changes `board`. Use `copy.deepcopy`.

```python
import copy

board = [["X", "O"], ["O", "X"]]
trial = copy.deepcopy(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
```

[Back to Exercise 20.25.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-25-3) &middot; [`sol_20_25_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_25_3.py)

</details>

### Solution 20.25.4 — Snapshotting weekly readings
{: #sol-20-25-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`readings.copy()` is shallow, so the nested lists remain shared and editing `snapshot` also edits `readings`. Use `copy.deepcopy`.

```python
import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = copy.deepcopy(readings)
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
```

[Back to Exercise 20.25.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-25-4) &middot; [`sol_20_25_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_25_4.py)

</details>

### Solution 20.25.5 — Cloning a recipe with sub-steps
{: #sol-20-25-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Slicing with `[:]` copies only the outer list; the nested step lists are shared, so appending through `clone` changes `recipe`. Use `copy.deepcopy`.

```python
import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = copy.deepcopy(recipe)
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
```

[Back to Exercise 20.25.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-25-5) &middot; [`sol_20_25_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_25_5.py)

</details>

## Solutions 20.26.1–20.26.5

### Solution 20.26.1 — Collecting quiz answers
{: #sol-20-26-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The default `sheet=[]` is created once and reused, so answers accumulate across calls. Default to `None` and make a fresh list inside.

```python
def record_answer(answer, sheet=None):
    if sheet is None:
        sheet = []
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
```

[Back to Exercise 20.26.1]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-26-1) &middot; [`sol_20_26_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_26_1.py)

</details>

### Solution 20.26.2 — Building a grocery list
{: #sol-20-26-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The mutable default `cart=[]` is shared between calls, so items pile up. Use `None` and create a new list inside the function.

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
```

[Back to Exercise 20.26.2]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-26-2) &middot; [`sol_20_26_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_26_2.py)

</details>

### Solution 20.26.3 — Logging a single temperature
{: #sol-20-26-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The default `log=[]` is created once and reused across calls, so readings accumulate. Default to `None` and build a fresh list.

```python
def log_reading(reading, log=None):
    if log is None:
        log = []
    log.append(reading)
    return log

print(log_reading(21.5))  # [21.5]
print(log_reading(19.0))  # [19.0]
```

[Back to Exercise 20.26.3]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-26-3) &middot; [`sol_20_26_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_26_3.py)

</details>

### Solution 20.26.4 — Tracking a player's scores
{: #sol-20-26-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The shared default `board=[]` keeps old scores between calls. Use `None` and create a new list inside the function.

```python
def new_scoreboard(score, board=None):
    if board is None:
        board = []
    board.append(score)
    return board

print(new_scoreboard(10))  # [10]
print(new_scoreboard(20))  # [20]
```

[Back to Exercise 20.26.4]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-26-4) &middot; [`sol_20_26_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_26_4.py)

</details>

### Solution 20.26.5 — Noting one ingredient
{: #sol-20-26-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The mutable default `items=[]` is reused on every call, so ingredients accumulate. Default to `None` and make a fresh list.

```python
def note_ingredient(name, items=None):
    if items is None:
        items = []
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
```

[Back to Exercise 20.26.5]({{ site.baseurl }}/ep/exercises/20-common-pitfalls/#ex-20-26-5) &middot; [`sol_20_26_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_20_26_5.py)

</details>

