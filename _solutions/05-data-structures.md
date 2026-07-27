---
title: "Chapter 5: Data Structures — Solutions"
short_title: "Ch. 5 — Data Structures"
layout: post
permalink: /ep/solutions/05-data-structures/
order: 1
chapter: 5
---

Worked solutions to the 50 *Find the Bug* exercises in [Chapter 5: Data Structures]({{ site.baseurl }}/ep/exercises/05-data-structures/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## int

### Solution 5.1.1 — Total points
{: #sol-5-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The third section was subtracted instead of added, giving 25 instead of 75. Change the `-` to `+` so all three sections are summed.

```python
section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 + section3
print(total)   # 75
```

[Back to Exercise 5.1.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-1-1) &middot; [`sol_5_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_1_1.py)

</details>

### Solution 5.1.2 — Students per team
{: #sol-5-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `/` operator always produces a float (6.0), but a whole number of students per team is wanted. Use integer division `//` to get the int 6.

```python
students = 30
teams = 5

per_team = students // teams
print(per_team)   # 6
```

[Back to Exercise 5.1.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-1-2) &middot; [`sol_5_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_1_2.py)

</details>

### Solution 5.1.3 — Seconds in an hour
{: #sol-5-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The two counts must be multiplied, not added; `60 + 60` gives 120, not 3600. Use `*`.

```python
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)   # 3600
```

[Back to Exercise 5.1.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-1-3) &middot; [`sol_5_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_1_3.py)

</details>

### Solution 5.1.4 — Counting by tens
{: #sol-5-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`"10"` is a string, so `count + "10"` raises a `TypeError` (you cannot add an int and a str). Use the int literal `10`.

```python
count = 100
count = count + 10
print(count)   # 110
```

[Back to Exercise 5.1.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-1-4) &middot; [`sol_5_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_1_4.py)

</details>

### Solution 5.1.5 — Apples per box
{: #sol-5-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`%` gives the remainder (2 leftover apples), not the number of full boxes. Use integer division `//` to get 3.

```python
apples = 17
per_box = 5

full_boxes = apples // per_box
print(full_boxes)   # 3
```

[Back to Exercise 5.1.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-1-5) &middot; [`sol_5_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_1_5.py)

</details>

## float

### Solution 5.2.1 — Average temperature
{: #sol-5-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Without parentheses, only `reading3 / 3` is divided (operator precedence), so the sum is wrong. Wrap the addition in parentheses before dividing.

```python
reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = (reading1 + reading2 + reading3) / 3
print(average)   # 22.0
```

[Back to Exercise 5.2.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-2-1) &middot; [`sol_5_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_2_1.py)

</details>

### Solution 5.2.2 — Splitting a bill
{: #sol-5-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`//` discards the fractional part, giving 12 instead of 12.5. Use true division `/` so the result is a float.

```python
bill = 50
people = 4

each = bill / people
print(each)   # 12.5
```

[Back to Exercise 5.2.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-2-2) &middot; [`sol_5_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_2_2.py)

</details>

### Solution 5.2.3 — Rounding a price
{: #sol-5-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`round(price)` with no second argument rounds to a whole number (3). Pass `2` to round to two decimal places.

```python
price = 3.14159
rounded = round(price, 2)
print(rounded)   # 3.14
```

[Back to Exercise 5.2.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-2-3) &middot; [`sol_5_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_2_3.py)

</details>

### Solution 5.2.4 — Half of a measurement
{: #sol-5-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The closing parenthesis of `print(...)` is missing, so the program will not parse. Add the `)` after `half`.

```python
length = 9.0
half = length / 2
print(half)   # 4.5
```

[Back to Exercise 5.2.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-2-4) &middot; [`sol_5_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_2_4.py)

</details>

### Solution 5.2.5 — Celsius to Fahrenheit
{: #sol-5-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Operator precedence makes `celsius * 9 / 5 - 32` subtract 32 instead of adding it, and the +32 must come after the multiply/divide. Add parentheses or use `+ 32`: the formula is `celsius * 9 / 5 + 32`.

```python
celsius = 100.0
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)   # 212.0
```

[Back to Exercise 5.2.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-2-5) &middot; [`sol_5_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_2_5.py)

</details>

## bool

### Solution 5.3.1 — Is it freezing?
{: #sol-5-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

"Below freezing" means less than 0, but the test used `>`, which is False for -5. Use `<` so the comparison returns True.

```python
temp = -5
is_freezing = temp < 0
print(is_freezing)   # True
```

[Back to Exercise 5.3.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-3-1) &middot; [`sol_5_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_3_1.py)

</details>

### Solution 5.3.2 — Passing grade
{: #sol-5-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`Passed` (capital P) is a different, undefined name, so printing it raises a `NameError`. Print the variable `passed`.

```python
grade = 72
passed = grade >= 60
print(passed)   # True
```

[Back to Exercise 5.3.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-3-2) &middot; [`sol_5_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_3_2.py)

</details>

### Solution 5.3.3 — Both lights on
{: #sol-5-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

"Both" requires `and`; `or` is True when either light is on. Use `and` so the result is False here.

```python
light1_on = True
light2_on = False

ready = light1_on and light2_on
print(ready)   # False
```

[Back to Exercise 5.3.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-3-3) &middot; [`sol_5_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_3_3.py)

</details>

### Solution 5.3.4 — Empty cart
{: #sol-5-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`is_empty = items = 0` is a chained assignment that sets `is_empty` to `0`, not the comparison you intended; it runs but prints `0`. Comparing values needs `==`, so write `is_empty = items == 0`.

```python
items = 0
is_empty = items == 0
print(is_empty)   # True
```

[Back to Exercise 5.3.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-3-4) &middot; [`sol_5_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_3_4.py)

</details>

### Solution 5.3.5 — Within speed limit
{: #sol-5-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Being within the limit means the speed is at or below it, but `>` tests the opposite. Use `<=` so 60 within 65 gives True.

```python
speed = 60
limit = 65

within_limit = speed <= limit
print(within_limit)   # True
```

[Back to Exercise 5.3.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-3-5) &middot; [`sol_5_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_3_5.py)

</details>

## Strings

### Solution 5.4.1 — First letter
{: #sol-5-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

String indexing starts at 0, so `city[1]` is the second letter ("o"). Use index `0` for the first letter.

```python
city = "Tokyo"
first = city[0]
print(first)   # T
```

[Back to Exercise 5.4.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-4-1) &middot; [`sol_5_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_4_1.py)

</details>

### Solution 5.4.2 — Shouting
{: #sol-5-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`word.upper` refers to the method without calling it, so it prints a method object, not the text. Add parentheses to call it: `word.upper()`.

```python
word = "hello"
loud = word.upper()
print(loud)   # HELLO
```

[Back to Exercise 5.4.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-4-2) &middot; [`sol_5_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_4_2.py)

</details>

### Solution 5.4.3 — Full name
{: #sol-5-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Concatenation does not insert a space, so the result is "MayaSingh". Add a space string between the names.

```python
first = "Maya"
last = "Singh"

full = first + " " + last
print(full)   # Maya Singh
```

[Back to Exercise 5.4.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-4-3) &middot; [`sol_5_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_4_3.py)

</details>

### Solution 5.4.4 — Length of a word
{: #sol-5-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`word()` tries to call the string as if it were a function, raising a `TypeError`. Pass the string itself to `len`.

```python
word = "science"
count = len(word)
print(count)   # 7
```

[Back to Exercise 5.4.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-4-4) &middot; [`sol_5_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_4_4.py)

</details>

### Solution 5.4.5 — Last three characters
{: #sol-5-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`code[-3]` is a single character ("7"), not the last three. Slice with `code[-3:]` to get "789".

```python
code = "ABC789"
last_three = code[-3:]
print(last_three)   # 789
```

[Back to Exercise 5.4.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-4-5) &middot; [`sol_5_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_4_5.py)

</details>

## None

### Solution 5.5.1 — No reading yet
{: #sol-5-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`None` is not the same as the string `"None"`, so the comparison is always False. Compare to the real `None` value with `is None`.

```python
reading = None
no_data = reading is None
print(no_data)   # True
```

[Back to Exercise 5.5.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-5-1) &middot; [`sol_5_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_5_1.py)

</details>

### Solution 5.5.2 — Default color
{: #sol-5-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function changes `color` but never returns it, so it returns `None`. Add a `return color` statement.

```python
def choose_color(color):
    if color is None:
        color = "blue"
    return color

print(choose_color(None))   # blue
```

[Back to Exercise 5.5.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-5-2) &middot; [`sol_5_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_5_2.py)

</details>

### Solution 5.5.3 — Checking for a value
{: #sol-5-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The test `is not None` is False when the value is `None`, so the program runs the wrong branch and prints "has value". Use `is None` so a `None` value prints "missing".

```python
favorite = None

if favorite is None:
    print("missing")
else:
    print("has value")
# expected: missing
```

[Back to Exercise 5.5.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-5-3) &middot; [`sol_5_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_5_3.py)

</details>

### Solution 5.5.4 — Length of nothing
{: #sol-5-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(None)` raises a `TypeError` because `None` has no length. Check for `None` first and use 0 in that case.

```python
temps = None
count = len(temps) if temps is not None else 0
print(count)   # 0
```

[Back to Exercise 5.5.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-5-4) &middot; [`sol_5_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_5_4.py)

</details>

### Solution 5.5.5 — Comparing to None
{: #sol-5-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`Not_set` (capital N) is undefined, so printing it raises a `NameError`. Print the variable `not_set`.

```python
username = None
not_set = username is None
print(not_set)   # True
```

[Back to Exercise 5.5.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-5-5) &middot; [`sol_5_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_5_5.py)

</details>

## Lists

### Solution 5.6.1 — First fruit
{: #sol-5-6-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

List indexing starts at 0, so `fruits[1]` is "banana". Use index `0` for the first fruit.

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
```

[Back to Exercise 5.6.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-6-1) &middot; [`sol_5_6_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_6_1.py)

</details>

### Solution 5.6.2 — Adding an item
{: #sol-5-6-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Lists have no `add` method, so this raises an `AttributeError`. Use `append` to add to a list.

```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(len(fruits))   # 4
```

[Back to Exercise 5.6.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-6-2) &middot; [`sol_5_6_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_6_2.py)

</details>

### Solution 5.6.3 — Last score
{: #sol-5-6-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The list has indexes 0, 1, 2, so `scores[3]` is out of range and raises an `IndexError`. The last item is at index 2 (or use `-1`).

```python
scores = [70, 95, 88]
print(scores[-1])   # 88
```

[Back to Exercise 5.6.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-6-3) &middot; [`sol_5_6_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_6_3.py)

</details>

### Solution 5.6.4 — Changing a value
{: #sol-5-6-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

Item assignment uses square brackets, not parentheses; `prices(1) = 5.0` is not valid Python. Use `prices[1] = 5.0`.

```python
prices = [2.0, 3.0, 4.0]
prices[1] = 5.0
print(prices)   # [2.0, 5.0, 4.0]
```

[Back to Exercise 5.6.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-6-4) &middot; [`sol_5_6_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_6_4.py)

</details>

### Solution 5.6.5 — How many items
{: #sol-5-6-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`len(shopping)` already gives 3; subtracting 1 makes it 2. Remove the `- 1`.

```python
shopping = ["milk", "eggs", "bread"]
count = len(shopping)
print(count)   # 3
```

[Back to Exercise 5.6.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-6-5) &middot; [`sol_5_6_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_6_5.py)

</details>

## Tuples

### Solution 5.7.1 — Map coordinates
{: #sol-5-7-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Index 0 is the latitude; `location[1]` returns the longitude. Use index `0`.

```python
location = (41.8781, -87.6298)
print(location[0])   # 41.8781
```

[Back to Exercise 5.7.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-7-1) &middot; [`sol_5_7_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_7_1.py)

</details>

### Solution 5.7.2 — A fixed pair
{: #sol-5-7-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Tuples are immutable, so `size[0] = 1280` raises a `TypeError`. You cannot change one element in place; build a new tuple instead.

```python
size = (1920, 1080)
size = (1280, size[1])
print(size)   # (1280, 1080)
```

[Back to Exercise 5.7.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-7-2) &middot; [`sol_5_7_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_7_2.py)

</details>

### Solution 5.7.3 — Unpacking coordinates
{: #sol-5-7-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Assigning the whole tuple to each name does not unpack it. Unpack both values at once with `lat, lon = coords`.

```python
coords = (35.7, 139.7)
lat, lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
```

[Back to Exercise 5.7.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-7-3) &middot; [`sol_5_7_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_7_3.py)

</details>

### Solution 5.7.4 — A single value
{: #sol-5-7-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`(42)` is just the number 42 in parentheses, not a tuple, so `len(single)` raises a `TypeError` on an int. A one-element tuple needs a trailing comma: `(42,)`.

```python
single = (42,)
print(len(single))   # 1
```

[Back to Exercise 5.7.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-7-4) &middot; [`sol_5_7_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_7_4.py)

</details>

### Solution 5.7.5 — Days in a tuple
{: #sol-5-7-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Index 1 is the second item ("Tue"); `days[2]` returns "Wed". Use index `1`.

```python
days = ("Mon", "Tue", "Wed")
print(days[1])   # Tue
```

[Back to Exercise 5.7.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-7-5) &middot; [`sol_5_7_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_7_5.py)

</details>

## Sets

### Solution 5.8.1 — Unique colors
{: #sol-5-8-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Square brackets create a list, which keeps the duplicate "red", so `len` is 4. Use curly braces to make a set, which drops duplicates and gives 3.

```python
colors = {"red", "blue", "red", "green"}
print(len(colors))   # 3
```

[Back to Exercise 5.8.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-8-1) &middot; [`sol_5_8_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_8_1.py)

</details>

### Solution 5.8.2 — Adding a member
{: #sol-5-8-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Sets have no `append` method, so this raises an `AttributeError`. Use `add` to put an item in a set.

```python
cities = {"New York", "London", "Tokyo"}
cities.add("Sydney")
print(len(cities))   # 4
```

[Back to Exercise 5.8.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-8-2) &middot; [`sol_5_8_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_8_2.py)

</details>

### Solution 5.8.3 — Is it a member?
{: #sol-5-8-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The program tests "yellow", which is not in the set, so it prints False. Test for "blue" to get True.

```python
colors = {"red", "blue", "green"}
print("blue" in colors)   # True
```

[Back to Exercise 5.8.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-8-3) &middot; [`sol_5_8_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_8_3.py)

</details>

### Solution 5.8.4 — Shared subjects
{: #sol-5-8-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`|` is union (all subjects from both); shared items need intersection `&`. Use `maya & leo` to get just `{"math"}`.

```python
maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya & leo
print(shared)   # {'math'}
```

[Back to Exercise 5.8.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-8-4) &middot; [`sol_5_8_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_8_4.py)

</details>

### Solution 5.8.5 — Building a set
{: #sol-5-8-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`{}` creates an empty dictionary, not a set, so `seen.add` raises an `AttributeError`. Use `set()` to create an empty set.

```python
seen = set()
seen.add("apple")
print(seen)   # {'apple'}
```

[Back to Exercise 5.8.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-8-5) &middot; [`sol_5_8_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_8_5.py)

</details>

## Dictionaries

### Solution 5.9.1 — Looking up a name
{: #sol-5-9-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Keys are case-sensitive; `"Name"` is not in the dict, so this raises a `KeyError`. Use the actual key `"name"`.

```python
student = {"name": "Maya", "grade": 10}
print(student["name"])   # Maya
```

[Back to Exercise 5.9.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-9-1) &middot; [`sol_5_9_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_9_1.py)

</details>

### Solution 5.9.2 — Updating a grade
{: #sol-5-9-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

Dictionary assignment uses square brackets, not parentheses; `student("grade") = 11` is invalid. Use `student["grade"] = 11`.

```python
student = {"name": "Maya", "grade": 10}
student["grade"] = 11
print(student["grade"])   # 11
```

[Back to Exercise 5.9.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-9-2) &middot; [`sol_5_9_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_9_2.py)

</details>

### Solution 5.9.3 — Missing key
{: #sol-5-9-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Indexing a missing key with `[]` raises a `KeyError`. Use `.get` with a default so it returns "not found" instead.

```python
student = {"name": "Maya", "grade": 10}
subject = student.get("favorite_subject", "not found")
print(subject)   # not found
```

[Back to Exercise 5.9.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-9-3) &middot; [`sol_5_9_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_9_3.py)

</details>

### Solution 5.9.4 — Safe default with get
{: #sol-5-9-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`Subject` (capital S) is undefined, so printing it raises a `NameError`. Print the variable `subject`.

```python
student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(subject)   # science
```

[Back to Exercise 5.9.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-9-4) &middot; [`sol_5_9_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_9_4.py)

</details>

### Solution 5.9.5 — Adding an entry
{: #sol-5-9-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`==` compares values; it does not store anything, so the key "phone" is never added and the next line raises a `KeyError`. Use a single `=` to assign the new entry.

```python
contact = {"name": "Leo"}
contact["phone"] = "555-0100"
print(contact["phone"])   # 555-0100
```

[Back to Exercise 5.9.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-9-5) &middot; [`sol_5_9_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_9_5.py)

</details>

## Variables and Types

### Solution 5.10.1 — Reading a number
{: #sol-5-10-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`age_text` is a string, so `age_text + 5` mixes str and int and raises a `TypeError`. Convert the text with `int()` before adding.

```python
age_text = "25"
age = int(age_text) + 5
print(age)   # 30
```

[Back to Exercise 5.10.1]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-10-1) &middot; [`sol_5_10_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_10_1.py)

</details>

### Solution 5.10.2 — Building a message
{: #sol-5-10-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

You cannot concatenate a str and an int, so this raises a `TypeError`. Convert the number with `str()` first.

```python
score = 90
message = "Score: " + str(score)
print(message)   # Score: 90
```

[Back to Exercise 5.10.2]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-10-2) &middot; [`sol_5_10_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_10_2.py)

</details>

### Solution 5.10.3 — Checking a type
{: #sol-5-10-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The price is a float, but the check compares against `int`, so it reports False. Compare against `float`.

```python
price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == float)   # True
```

[Back to Exercise 5.10.3]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-10-3) &middot; [`sol_5_10_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_10_3.py)

</details>

### Solution 5.10.4 — Converting to float
{: #sol-5-10-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`int("2.5")` raises a `ValueError` because the text is not a whole number. Use `float()` to convert it.

```python
weight_text = "2.5"
weight = float(weight_text)
print(weight * 2)   # 5.0
```

[Back to Exercise 5.10.4]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-10-4) &middot; [`sol_5_10_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_10_4.py)

</details>

### Solution 5.10.5 — Whole-number average
{: #sol-5-10-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`average` is wrapped in `str()`, so `int("85.5")` raises a `ValueError`. Keep the average numeric and apply `int()` directly.

```python
score1 = 80
score2 = 91

average = (score1 + score2) / 2
print(int(average))   # 85
```

[Back to Exercise 5.10.5]({{ site.baseurl }}/ep/exercises/05-data-structures/#ex-5-10-5) &middot; [`sol_5_10_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_5_10_5.py)

</details>

