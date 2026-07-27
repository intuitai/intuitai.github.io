---
title: "Chapter 9: Control Flow — Solutions"
short_title: "Ch. 9 — Control Flow"
layout: post
permalink: /ep/solutions/09-control-flow/
order: 5
chapter: 9
---

Worked solutions to the 55 *Find the Bug* exercises in [Chapter 9: Control Flow]({{ site.baseurl }}/ep/exercises/09-control-flow/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 9.1.1–9.1.5

### Solution 9.1.1 — Grading with elif
{: #sol-9-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `else` line is missing its colon, so Python cannot parse the block. Adding the colon fixes it.

```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Needs improvement")
```

[Back to Exercise 9.1.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-1-1) &middot; [`sol_9_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_1_1.py)

</details>

### Solution 9.1.2 — Temperature category
{: #sol-9-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The body of the first `if` is not indented, so Python raises an `IndentationError`. Indenting the `print` four spaces fixes it.

```python
temp_c = 36.5

if temp_c > 35:
    print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
```

[Back to Exercise 9.1.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-1-2) &middot; [`sol_9_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_1_2.py)

</details>

### Solution 9.1.3 — Independent checks that should be alternatives
{: #sol-9-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The second test starts a new `if` instead of chaining with `elif`, so its `else` attaches to the second `if` only; an acidic value (pH 6.0) makes the first `if` print `Acidic` and the second `else` also print `Basic`. Using `elif` makes the three cases mutually exclusive.

```python
ph = 6.0

if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")
```

[Back to Exercise 9.1.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-1-3) &middot; [`sol_9_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_1_3.py)

</details>

### Solution 9.1.4 — Pass or fail
{: #sol-9-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `else` is indented as if it were inside the `if` body, which is illegal. Aligning `else` with `if` fixes it.

```python
score = 75

if score >= 60:
    print("Pass")
else:
    print("Fail")
```

[Back to Exercise 9.1.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-1-4) &middot; [`sol_9_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_1_4.py)

</details>

### Solution 9.1.5 — Ticket price by age
{: #sol-9-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `print` is indented inside the `else` branch, so it only runs for the full price; the child's price is never shown. Moving `print` out to run after the `if`/`else` fixes it.

```python
age = 10

if age < 12:
    price = 5
else:
    price = 12

print("Ticket price:", price)
```

[Back to Exercise 9.1.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-1-5) &middot; [`sol_9_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_1_5.py)

</details>

## Solutions 9.2.1–9.2.5

### Solution 9.2.1 — Exact match
{: #sol-9-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A single `=` is assignment, not comparison, and is not allowed in an `if` condition. Use `==` to compare.

```python
answer = 42

if answer == 42:
    print("Correct")
else:
    print("Try again")
```

[Back to Exercise 9.2.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-2-1) &middot; [`sol_9_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_2_1.py)

</details>

### Solution 9.2.2 — Freezing point
{: #sol-9-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`<` excludes 0 itself, but water freezes *at* 0 too. Using `<=` includes the freezing point.

```python
temp_c = 0

if temp_c <= 0:
    print("Frozen")
else:
    print("Liquid")
```

[Back to Exercise 9.2.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-2-2) &middot; [`sol_9_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_2_2.py)

</details>

### Solution 9.2.3 — Not equal
{: #sol-9-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The condition should test “not 0” but uses `==`, so it prints `Sold out` exactly when seats is 0. Use `!=` to match the intended meaning.

```python
seats_left = 0

if seats_left != 0:
    print("Sold out")
```

[Back to Exercise 9.2.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-2-3) &middot; [`sol_9_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_2_3.py)

</details>

### Solution 9.2.4 — Speed limit check
{: #sol-9-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

“At most 60” includes 60, but `<` excludes it, so a car at the limit is wrongly flagged. Use `<=`.

```python
speed = 60
limit = 60

if speed <= limit:
    print("OK")
else:
    print("Too fast")
```

[Back to Exercise 9.2.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-2-4) &middot; [`sol_9_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_2_4.py)

</details>

### Solution 9.2.5 — Adult check
{: #sol-9-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

“18 or older” includes 18, but `>` excludes it. Use `>=`.

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

[Back to Exercise 9.2.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-2-5) &middot; [`sol_9_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_2_5.py)

</details>

## Solutions 9.3.1–9.3.5

### Solution 9.3.1 — Entry rules
{: #sol-9-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`or` allows entry when *either* condition holds, but both age and ID are required. Using `and` enforces both.

```python
age = 20
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

[Back to Exercise 9.3.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-3-1) &middot; [`sol_9_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_3_1.py)

</details>

### Solution 9.3.2 — Weekend check
{: #sol-9-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A day cannot equal both `Saturday` and `Sunday`, so the `and` condition is never true and nothing prints. The cases are alternatives, so use `or`.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Relax")
# expected: Relax
```

[Back to Exercise 9.3.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-3-2) &middot; [`sol_9_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_3_2.py)

</details>

### Solution 9.3.3 — Comfortable room
{: #sol-9-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

With `or`, almost every temperature satisfies at least one side, so even 30 degrees prints “Comfortable”. The range requires *both* bounds, so use `and`.

```python
temp_c = 30

if temp_c >= 20 and temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
```

[Back to Exercise 9.3.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-3-3) &middot; [`sol_9_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_3_3.py)

</details>

### Solution 9.3.4 — Out of stock
{: #sol-9-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

`not in_stock = True` mixes `not` with an assignment, which is invalid. The intent is simply to test the negation, so write `if not in_stock:`.

```python
in_stock = False

if not in_stock:
    print("Reorder")
```

[Back to Exercise 9.3.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-3-4) &middot; [`sol_9_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_3_4.py)

</details>

### Solution 9.3.5 — Free shipping
{: #sol-9-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Free shipping should apply when *either* condition holds, but `and` requires both, so a member with a $30 order is wrongly charged. Using `or` matches the rule.

```python
total = 30
is_member = True

if total >= 50 or is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
```

[Back to Exercise 9.3.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-3-5) &middot; [`sol_9_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_3_5.py)

</details>

## Solutions 9.4.1–9.4.5

### Solution 9.4.1 — Sum of a list
{: #sol-9-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`total = price` overwrites the running sum each pass instead of adding to it, leaving only the last price. Use `total += price` to accumulate.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print("Total:", total)
```

[Back to Exercise 9.4.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-4-1) &middot; [`sol_9_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_4_1.py)

</details>

### Solution 9.4.2 — Counting vowels
{: #sol-9-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The count is correct, but `print(count + 1)` adds one extra at the end. Print `count` itself.

```python
word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count)
```

[Back to Exercise 9.4.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-4-2) &middot; [`sol_9_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_4_2.py)

</details>

### Solution 9.4.3 — Printing each fruit
{: #sol-9-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `for` statement is missing its colon. Adding it fixes the parse error.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

[Back to Exercise 9.4.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-4-3) &middot; [`sol_9_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_4_3.py)

</details>

### Solution 9.4.4 — Average of readings
{: #sol-9-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(reading)` uses the loop variable (the last item, an integer) instead of the list, raising a `TypeError`. Use `len(readings)`.

```python
readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(readings)
print(average)
```

[Back to Exercise 9.4.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-4-4) &middot; [`sol_9_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_4_4.py)

</details>

### Solution 9.4.5 — Largest measurement
{: #sol-9-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The comparison `<` keeps the smallest value, not the largest. To track the maximum, replace it when the current value is *greater*, using `>`.

```python
distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance > largest:
        largest = distance

print(largest)
```

[Back to Exercise 9.4.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-4-5) &middot; [`sol_9_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_4_5.py)

</details>

## Solutions 9.5.1–9.5.5

### Solution 9.5.1 — Counting to five
{: #sol-9-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range` stops before its end value, so `range(1, 5)` yields 1–4. To reach 5, use `range(1, 6)`.

```python
for number in range(1, 6):
    print(number)
```

[Back to Exercise 9.5.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-5-1) &middot; [`sol_9_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_5_1.py)

</details>

### Solution 9.5.2 — Even numbers
{: #sol-9-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A step of 1 prints every number, not just the evens. The step should be 2.

```python
for number in range(2, 11, 2):
    print(number)
```

[Back to Exercise 9.5.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-5-2) &middot; [`sol_9_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_5_2.py)

</details>

### Solution 9.5.3 — Counting down
{: #sol-9-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

To count downward, `range` needs a negative step; `range(5, 0)` counts *up* and produces nothing because 5 is already past 0. Use `range(5, 0, -1)`.

```python
for number in range(5, 0, -1):
    print(number)
```

[Back to Exercise 9.5.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-5-3) &middot; [`sol_9_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_5_3.py)

</details>

### Solution 9.5.4 — Sum of first ten numbers
{: #sol-9-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range(1, 10)` stops at 9, so 10 is left out and the total is 45. Use `range(1, 11)` to include 10.

```python
total = 0

for number in range(1, 11):
    total += number

print(total)
```

[Back to Exercise 9.5.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-5-4) &middot; [`sol_9_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_5_4.py)

</details>

### Solution 9.5.5 — Three repetitions
{: #sol-9-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range(3)` runs three times, but the extra `print(count)` also prints the index each pass, which was not intended. Removing that line prints `Hello` three times.

```python
for count in range(3):
    print("Hello")
```

[Back to Exercise 9.5.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-5-5) &middot; [`sol_9_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_5_5.py)

</details>

## Solutions 9.6.1–9.6.5

### Solution 9.6.1 — Counting with while
{: #sol-9-6-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The loop never updates `count`, so the condition stays true forever—an infinite loop. Incrementing `count` each pass lets it terminate.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

[Back to Exercise 9.6.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-6-1) &middot; [`sol_9_6_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_6_1.py)

</details>

### Solution 9.6.2 — Countdown
{: #sol-9-6-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`count += 1` moves away from the stop condition, so `count > 0` never becomes false—an infinite loop. Use `count -= 1` to count down.

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("Liftoff")
```

[Back to Exercise 9.6.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-6-2) &middot; [`sol_9_6_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_6_2.py)

</details>

### Solution 9.6.3 — Doubling savings
{: #sol-9-6-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`balance + 2` adds a fixed 2 each pass instead of *doubling*, so the balance grows 1, 3, 5, 7, ... and the values are wrong. Multiplying by 2 doubles it as intended.

```python
balance = 1

while balance < 8:
    print(balance)
    balance = balance * 2
```

[Back to Exercise 9.6.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-6-3) &middot; [`sol_9_6_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_6_3.py)

</details>

### Solution 9.6.4 — Loop condition
{: #sol-9-6-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`while count < 5` stops after printing 4, so 5 is never reached. Use `<=` to include 5.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

[Back to Exercise 9.6.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-6-4) &middot; [`sol_9_6_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_6_4.py)

</details>

### Solution 9.6.5 — Sum until limit
{: #sol-9-6-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`number` is incremented *before* being added, so the loop adds 2+3+4+5 = 14 and skips 1. Adding first, then incrementing, sums 1+2+3+4 = 10.

```python
total = 0
number = 1

while total < 10:
    total += number
    number += 1

print(total)
```

[Back to Exercise 9.6.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-6-5) &middot; [`sol_9_6_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_6_5.py)

</details>

## Solutions 9.7.1–9.7.5

### Solution 9.7.1 — Stop at the target
{: #sol-9-7-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`continue` only skips 3 and keeps going (printing 4, 5), but the program should stop entirely before 3. Use `break` to exit the loop.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

[Back to Exercise 9.7.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-7-1) &middot; [`sol_9_7_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_7_1.py)

</details>

### Solution 9.7.2 — First over budget
{: #sol-9-7-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`break` is not indented inside the `if`, so it runs on the very first item and the loop stops before finding 150. Indenting `break` under the `if` makes it exit only after a match.

```python
expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
        break
```

[Back to Exercise 9.7.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-7-2) &middot; [`sol_9_7_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_7_2.py)

</details>

### Solution 9.7.3 — Search for a name
{: #sol-9-7-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`brake` is a misspelling of `break`, so Python raises a `NameError`. Correcting the keyword fixes it.

```python
names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        break
```

[Back to Exercise 9.7.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-7-3) &middot; [`sol_9_7_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_7_3.py)

</details>

### Solution 9.7.4 — First even number
{: #sol-9-7-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`break` runs before the `print`, so nothing is ever shown. Print the number first, then break.

```python
numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
```

[Back to Exercise 9.7.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-7-4) &middot; [`sol_9_7_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_7_4.py)

</details>

### Solution 9.7.5 — Stop at zero
{: #sol-9-7-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`continue` merely skips the 0 and keeps going (printing 3 afterward), but the loop should stop at 0. Use `break`.

```python
readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        break
    print(reading)
```

[Back to Exercise 9.7.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-7-5) &middot; [`sol_9_7_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_7_5.py)

</details>

## Solutions 9.8.1–9.8.5

### Solution 9.8.1 — Skip the empty entries
{: #sol-9-8-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`break` stops the loop at the first empty string, so "dog" is never printed. To skip just the empty entries and continue, use `continue`.

```python
words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        continue
    print(word)
```

[Back to Exercise 9.8.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-8-1) &middot; [`sol_9_8_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_8_1.py)

</details>

### Solution 9.8.2 — Skip one value
{: #sol-9-8-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`pass` does nothing, so 3 is still printed. To actually skip it, use `continue`.

```python
for number in range(1, 7):
    if number == 3:
        continue
    print(number)
```

[Back to Exercise 9.8.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-8-2) &middot; [`sol_9_8_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_8_2.py)

</details>

### Solution 9.8.3 — Sum positive numbers
{: #sol-9-8-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `continue` after `total += number` is harmless, but `print(total + 1)` adds an extra 1, giving 10 instead of 9. Printing `total` gives the correct sum.

```python
numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number

print(total)
```

[Back to Exercise 9.8.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-8-3) &middot; [`sol_9_8_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_8_3.py)

</details>

### Solution 9.8.4 — Skip the indentation
{: #sol-9-8-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `continue` under the `if` is not indented, so Python raises an `IndentationError`. Indenting it inside the `if` fixes the parse.

```python
for number in range(1, 7):
    if number % 2 == 0:
        continue
    print(number)
```

[Back to Exercise 9.8.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-8-4) &middot; [`sol_9_8_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_8_4.py)

</details>

### Solution 9.8.5 — Skip a specific student
{: #sol-9-8-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The condition skips everyone *except* Leo, so only Leo is printed—the opposite of what we want. Skip when the name *is* Leo by using `==`.

```python
names = ["Ana", "Leo", "Sam"]

for name in names:
    if name == "Leo":
        continue
    print(name)
```

[Back to Exercise 9.8.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-8-5) &middot; [`sol_9_8_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_8_5.py)

</details>

## Solutions 9.9.1–9.9.5

### Solution 9.9.1 — Placeholder for later
{: #sol-9-9-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `if` body is empty, so Python raises an `IndentationError`. A placeholder body needs `pass`.

```python
for item in [1, 2, 3]:
    if item == 2:
        pass
    print(item)
```

[Back to Exercise 9.9.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-9-1) &middot; [`sol_9_9_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_9_1.py)

</details>

### Solution 9.9.2 — Empty function
{: #sol-9-9-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A function with an empty body is illegal; Python raises an `IndentationError`. Adding `pass` as the placeholder body fixes it.

```python
def future_feature():
    pass

future_feature()
print("Done")
```

[Back to Exercise 9.9.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-9-2) &middot; [`sol_9_9_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_9_2.py)

</details>

### Solution 9.9.3 — Doing nothing where logic was needed
{: #sol-9-9-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The loop body is left as `pass`, so nothing is added and the total stays 0. The real work—accumulating the prices—must replace the placeholder.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(total)
```

[Back to Exercise 9.9.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-9-3) &middot; [`sol_9_9_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_9_3.py)

</details>

### Solution 9.9.4 — Placeholder branch
{: #sol-9-9-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

After `pass` (which does nothing), the indented `print(reading)` still runs, so negative readings are printed too. Removing that stray `print` leaves the branch as a true placeholder.

```python
readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
    else:
        print(reading)
```

[Back to Exercise 9.9.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-9-4) &middot; [`sol_9_9_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_9_4.py)

</details>

### Solution 9.9.5 — Stub class
{: #sol-9-9-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`pas` is a typo for the keyword `pass`; Python reads it as a reference to an undefined name, so executing the class body raises a `NameError`. Correct the spelling to `pass`.

```python
class Sensor:
    pass

print("Ready")
```

[Back to Exercise 9.9.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-9-5) &middot; [`sol_9_9_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_9_5.py)

</details>

## Solutions 9.10.1–9.10.5

### Solution 9.10.1 — Matching a command
{: #sol-9-10-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The first `case` line is missing its colon. Adding it fixes the parse.

```python
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

[Back to Exercise 9.10.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-10-1) &middot; [`sol_9_10_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_10_1.py)

</details>

### Solution 9.10.2 — Weekend or weekday
{: #sol-9-10-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

In a `case` pattern, alternatives are joined with `|`, not the keyword `or`. Using `|` fixes the pattern.

```python
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
```

[Back to Exercise 9.10.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-10-2) &middot; [`sol_9_10_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_10_2.py)

</details>

### Solution 9.10.3 — Locating a point
{: #sol-9-10-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The catch-all `(x, y)` pattern matches *any* pair, so it is reached before the specific y-axis case and (0, 5) is wrongly labelled “Somewhere else”. The general pattern must come last, after the specific ones.

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On the y-axis at", y)
    case (x, y):
        print("Somewhere else:", x, y)
```

[Back to Exercise 9.10.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-10-3) &middot; [`sol_9_10_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_10_3.py)

</details>

### Solution 9.10.4 — Default case
{: #sol-9-10-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`case "_"` matches the literal string `"_"`, not “anything else”. The wildcard default is the bare `_` with no quotes.

```python
command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

[Back to Exercise 9.10.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-10-4) &middot; [`sol_9_10_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_10_4.py)

</details>

### Solution 9.10.5 — Traffic light
{: #sol-9-10-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The default case builds the string `"Unknown"` but never prints it, so an unrecognized colour produces no output. Adding `print` produces the expected output.

```python
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
```

[Back to Exercise 9.10.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-10-5) &middot; [`sol_9_10_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_10_5.py)

</details>

## Solutions 9.11.1–9.11.5

### Solution 9.11.1 — Even check
{: #sol-9-11-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function computes `number % 2 == 0` but never returns it, so it returns `None`. Adding `return` sends the result back.

```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))
```

[Back to Exercise 9.11.1]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-11-1) &middot; [`sol_9_11_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_11_1.py)

</details>

### Solution 9.11.2 — Describe a number
{: #sol-9-11-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The negative branch builds the string `"negative"` but never returns it, so `describe(-3)` falls off that branch and returns `None`. Adding `return` fixes it.

```python
def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(describe(-3))
```

[Back to Exercise 9.11.2]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-11-2) &middot; [`sol_9_11_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_11_2.py)

</details>

### Solution 9.11.3 — First match returns
{: #sol-9-11-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function `print`s the match instead of returning it, so `first_big` returns `None`. Replacing `print` with `return` sends the value back to the caller.

```python
def first_big(numbers):
    for number in numbers:
        if number > 10:
            return number

print(first_big([4, 15, 22]))
```

[Back to Exercise 9.11.3]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-11-3) &middot; [`sol_9_11_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_11_3.py)

</details>

### Solution 9.11.4 — Total with tax
{: #sol-9-11-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function returns `price` before computing the total, so the line after `return` never runs. Returning `price + tax` gives the taxed total.

```python
def with_tax(price):
    tax = price * 0.10
    total = price + tax
    return total

print(with_tax(100))
```

[Back to Exercise 9.11.4]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-11-4) &middot; [`sol_9_11_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_11_4.py)

</details>

### Solution 9.11.5 — Absolute value
{: #sol-9-11-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

When the number is not negative there is no `return`, so the function falls off the end and returns `None`. Adding an `else` (or a final `return number`) handles the non-negative case.

```python
def absolute(number):
    if number < 0:
        return -number
    else:
        return number

print(absolute(7))
```

[Back to Exercise 9.11.5]({{ site.baseurl }}/ep/exercises/09-control-flow/#ex-9-11-5) &middot; [`sol_9_11_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_9_11_5.py)

</details>

