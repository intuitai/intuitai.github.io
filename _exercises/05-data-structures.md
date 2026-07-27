---
title: "Chapter 5: Data Structures"
short_title: "Ch. 5 — Data Structures"
layout: post
permalink: /ep/exercises/05-data-structures/
order: 1
chapter: 5
exercise_count: 50
---

50 *Find the Bug* exercises from Chapter 5 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 5 solutions]({{ site.baseurl }}/ep/solutions/05-data-structures/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## int

### Exercise 5.1.1 — Total points
{: #ex-5-1-1 }

A quiz has 3 sections worth 20, 30, and 25 points. The program should print the total, 75.

```python
section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 - section3
print(total)   # 75
```

[Solution 5.1.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-1) &middot; [`ex_5_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_1_1.py)

### Exercise 5.1.2 — Students per team
{: #ex-5-1-2 }

Thirty students are split evenly into 5 teams. The program should print the whole number 6.

```python
students = 30
teams = 5

per_team = students / teams
print(per_team)   # 6
```

[Solution 5.1.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-2) &middot; [`ex_5_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_1_2.py)

### Exercise 5.1.3 — Seconds in an hour
{: #ex-5-1-3 }

There are 60 seconds in a minute and 60 minutes in an hour. The program should print 3600.

```python
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute + minutes_per_hour
print(seconds_per_hour)   # 3600
```

[Solution 5.1.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-3) &middot; [`ex_5_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_1_3.py)

### Exercise 5.1.4 — Counting by tens
{: #ex-5-1-4 }

The program should add 10 to a starting count and print 110.

```python
count = 100
count = count + "10"
print(count)   # 110
```

[Solution 5.1.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-4) &middot; [`ex_5_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_1_4.py)

### Exercise 5.1.5 — Apples per box
{: #ex-5-1-5 }

You have 17 apples and want 5 per box. The program should print how many full boxes (3) you can fill.

```python
apples = 17
per_box = 5

full_boxes = apples % per_box
print(full_boxes)   # 3
```

[Solution 5.1.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-5) &middot; [`ex_5_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_1_5.py)

## float

### Exercise 5.2.1 — Average temperature
{: #ex-5-2-1 }

Three readings are 20.0, 22.0, and 24.0 degrees. The program should print the average, 22.0.

```python
reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = reading1 + reading2 + reading3 / 3
print(average)   # 22.0
```

[Solution 5.2.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-2-1) &middot; [`ex_5_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_2_1.py)

### Exercise 5.2.2 — Splitting a bill
{: #ex-5-2-2 }

A 50-dollar bill is split between 4 people. The program should print 12.5.

```python
bill = 50
people = 4

each = bill // people
print(each)   # 12.5
```

[Solution 5.2.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-2-2) &middot; [`ex_5_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_2_2.py)

### Exercise 5.2.3 — Rounding a price
{: #ex-5-2-3 }

A price of 3.14159 dollars should be rounded to 2 decimal places, printing 3.14.

```python
price = 3.14159
rounded = round(price)
print(rounded)   # 3.14
```

[Solution 5.2.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-2-3) &middot; [`ex_5_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_2_3.py)

### Exercise 5.2.4 — Half of a measurement
{: #ex-5-2-4 }

A board is 9.0 meters long. The program should print half its length, 4.5.

```python
length = 9.0
half = length / 2
print(half   # 4.5
```

[Solution 5.2.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-2-4) &middot; [`ex_5_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_2_4.py)

### Exercise 5.2.5 — Celsius to Fahrenheit
{: #ex-5-2-5 }

The program converts 100.0 degrees Celsius to Fahrenheit and should print 212.0.

```python
celsius = 100.0
fahrenheit = celsius * 9 / 5 - 32
print(fahrenheit)   # 212.0
```

[Solution 5.2.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-2-5) &middot; [`ex_5_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_2_5.py)

## bool

### Exercise 5.3.1 — Is it freezing?
{: #ex-5-3-1 }

Water freezes at 0 degrees Celsius. The program should report `True` when the temperature is below freezing. With temp = -5 it should print True.

```python
temp = -5
is_freezing = temp > 0
print(is_freezing)   # True
```

[Solution 5.3.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-3-1) &middot; [`ex_5_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_3_1.py)

### Exercise 5.3.2 — Passing grade
{: #ex-5-3-2 }

A grade of 60 or more passes. With a grade of 72, the program should print `True`.

```python
grade = 72
passed = grade >= 60
print(Passed)   # True
```

[Solution 5.3.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-3-2) &middot; [`ex_5_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_3_2.py)

### Exercise 5.3.3 — Both lights on
{: #ex-5-3-3 }

A room is "ready" only if both lights are on. The program should print `False` here, since one light is off.

```python
light1_on = True
light2_on = False

ready = light1_on or light2_on
print(ready)   # False
```

[Solution 5.3.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-3-3) &middot; [`ex_5_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_3_3.py)

### Exercise 5.3.4 — Empty cart
{: #ex-5-3-4 }

A cart is empty when it has 0 items. The program should print `True`.

```python
items = 0
is_empty = items = 0
print(is_empty)   # True
```

[Solution 5.3.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-3-4) &middot; [`ex_5_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_3_4.py)

### Exercise 5.3.5 — Within speed limit
{: #ex-5-3-5 }

The limit is 65. A car going 60 is within the limit, so the program should print `True`.

```python
speed = 60
limit = 65

within_limit = speed > limit
print(within_limit)   # True
```

[Solution 5.3.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-3-5) &middot; [`ex_5_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_3_5.py)

## Strings

### Exercise 5.4.1 — First letter
{: #ex-5-4-1 }

The program should print the first letter of a city name: T.

```python
city = "Tokyo"
first = city[1]
print(first)   # T
```

[Solution 5.4.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-4-1) &middot; [`ex_5_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_4_1.py)

### Exercise 5.4.2 — Shouting
{: #ex-5-4-2 }

The program should print a greeting in all capitals: HELLO.

```python
word = "hello"
loud = word.upper
print(loud)   # HELLO
```

[Solution 5.4.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-4-2) &middot; [`ex_5_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_4_2.py)

### Exercise 5.4.3 — Full name
{: #ex-5-4-3 }

The program should join a first and last name with a space: "Maya Singh".

```python
first = "Maya"
last = "Singh"

full = first + last
print(full)   # Maya Singh
```

[Solution 5.4.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-4-3) &middot; [`ex_5_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_4_3.py)

### Exercise 5.4.4 — Length of a word
{: #ex-5-4-4 }

The program should print the number of letters in "science": 7.

```python
word = "science"
count = len(word())
print(count)   # 7
```

[Solution 5.4.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-4-4) &middot; [`ex_5_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_4_4.py)

### Exercise 5.4.5 — Last three characters
{: #ex-5-4-5 }

The program should print the last three characters of a code: "789".

```python
code = "ABC789"
last_three = code[-3]
print(last_three)   # 789
```

[Solution 5.4.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-4-5) &middot; [`ex_5_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_4_5.py)

## None

### Exercise 5.5.1 — No reading yet
{: #ex-5-5-1 }

A sensor has no reading. The program should print `True` because the reading is `None`.

```python
reading = None
no_data = reading == "None"
print(no_data)   # True
```

[Solution 5.5.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-5-1) &middot; [`ex_5_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_5_1.py)

### Exercise 5.5.2 — Default color
{: #ex-5-5-2 }

The function should return a default color when none is given. Calling it with nothing should print "blue".

```python
def choose_color(color):
    if color is None:
        color = "blue"

print(choose_color(None))   # blue
```

[Solution 5.5.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-5-2) &middot; [`ex_5_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_5_2.py)

### Exercise 5.5.3 — Checking for a value
{: #ex-5-5-3 }

When a value is `None`, the program should print "missing".

```python
favorite = None

if favorite is not None:
    print("missing")
else:
    print("has value")
# expected: missing
```

[Solution 5.5.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-5-3) &middot; [`ex_5_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_5_3.py)

### Exercise 5.5.4 — Length of nothing
{: #ex-5-5-4 }

A list of temperatures has not been filled in yet, so it is `None`. The program tries to count it and should instead detect the missing list and print 0.

```python
temps = None
count = len(temps)
print(count)   # 0
```

[Solution 5.5.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-5-4) &middot; [`ex_5_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_5_4.py)

### Exercise 5.5.5 — Comparing to None
{: #ex-5-5-5 }

The program should check whether a username has been set, printing `True` when it is still `None`.

```python
username = None
not_set = username is None
print(Not_set)   # True
```

[Solution 5.5.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-5-5) &middot; [`ex_5_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_5_5.py)

## Lists

### Exercise 5.6.1 — First fruit
{: #ex-5-6-1 }

The program should print the first fruit in the list: "apple".

```python
fruits = ["apple", "banana", "orange"]
print(fruits[1])   # apple
```

[Solution 5.6.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-6-1) &middot; [`ex_5_6_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_6_1.py)

### Exercise 5.6.2 — Adding an item
{: #ex-5-6-2 }

The program should add "grape" to the list and print 4 items in total.

```python
fruits = ["apple", "banana", "orange"]
fruits.add("grape")
print(len(fruits))   # 4
```

[Solution 5.6.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-6-2) &middot; [`ex_5_6_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_6_2.py)

### Exercise 5.6.3 — Last score
{: #ex-5-6-3 }

The program should print the last score in the list: 88.

```python
scores = [70, 95, 88]
print(scores[3])   # 88
```

[Solution 5.6.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-6-3) &middot; [`ex_5_6_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_6_3.py)

### Exercise 5.6.4 — Changing a value
{: #ex-5-6-4 }

The program should change the second price to 5.0 and print the list.

```python
prices = [2.0, 3.0, 4.0]
prices(1) = 5.0
print(prices)   # [2.0, 5.0, 4.0]
```

[Solution 5.6.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-6-4) &middot; [`ex_5_6_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_6_4.py)

### Exercise 5.6.5 — How many items
{: #ex-5-6-5 }

The program should print how many items are in the shopping list: 3.

```python
shopping = ["milk", "eggs", "bread"]
count = len(shopping) - 1
print(count)   # 3
```

[Solution 5.6.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-6-5) &middot; [`ex_5_6_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_6_5.py)

## Tuples

### Exercise 5.7.1 — Map coordinates
{: #ex-5-7-1 }

A location is stored as a (latitude, longitude) tuple. The program should print the latitude, 41.8781.

```python
location = (41.8781, -87.6298)
print(location[1])   # 41.8781
```

[Solution 5.7.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-7-1) &middot; [`ex_5_7_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_7_1.py)

### Exercise 5.7.2 — A fixed pair
{: #ex-5-7-2 }

This program should change the width to 1280 and print `(1280, 1080)`.

```python
size = (1920, 1080)
size[0] = 1280
print(size)   # expected: (1280, 1080)
```

[Solution 5.7.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-7-2) &middot; [`ex_5_7_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_7_2.py)

### Exercise 5.7.3 — Unpacking coordinates
{: #ex-5-7-3 }

The program should unpack a tuple into two variables and print "lat 35.7, lon 139.7".

```python
coords = (35.7, 139.7)
lat = coords
lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
```

[Solution 5.7.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-7-3) &middot; [`ex_5_7_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_7_3.py)

### Exercise 5.7.4 — A single value
{: #ex-5-7-4 }

The program should make a one-element tuple holding the number 42 and print its length, 1.

```python
single = (42)
print(len(single))   # 1
```

[Solution 5.7.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-7-4) &middot; [`ex_5_7_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_7_4.py)

### Exercise 5.7.5 — Days in a tuple
{: #ex-5-7-5 }

A tuple holds three weekday names. The program should print the second one, "Tue".

```python
days = ("Mon", "Tue", "Wed")
print(days[2])   # Tue
```

[Solution 5.7.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-7-5) &middot; [`ex_5_7_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_7_5.py)

## Sets

### Exercise 5.8.1 — Unique colors
{: #ex-5-8-1 }

A set removes duplicates. The program should print how many unique colors there are: 3.

```python
colors = ["red", "blue", "red", "green"]
print(len(colors))   # 3
```

[Solution 5.8.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-8-1) &middot; [`ex_5_8_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_8_1.py)

### Exercise 5.8.2 — Adding a member
{: #ex-5-8-2 }

The program should add "Sydney" to the set of cities and print 4 members in total.

```python
cities = {"New York", "London", "Tokyo"}
cities.append("Sydney")
print(len(cities))   # 4
```

[Solution 5.8.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-8-2) &middot; [`ex_5_8_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_8_2.py)

### Exercise 5.8.3 — Is it a member?
{: #ex-5-8-3 }

The program should check whether "blue" is in the set and print `True`.

```python
colors = {"red", "blue", "green"}
print("yellow" in colors)   # True
```

[Solution 5.8.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-8-3) &middot; [`ex_5_8_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_8_3.py)

### Exercise 5.8.4 — Shared subjects
{: #ex-5-8-4 }

Two students list their subjects. The program should print the subjects they share: {"math"}.

```python
maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya | leo
print(shared)   # {'math'}
```

[Solution 5.8.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-8-4) &middot; [`ex_5_8_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_8_4.py)

### Exercise 5.8.5 — Building a set
{: #ex-5-8-5 }

The program should start with an empty set, add one item, and print the set with that item.

```python
seen = {}
seen.add("apple")
print(seen)   # {'apple'}
```

[Solution 5.8.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-8-5) &middot; [`ex_5_8_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_8_5.py)

## Dictionaries

### Exercise 5.9.1 — Looking up a name
{: #ex-5-9-1 }

A student record stores a name. The program should print "Maya".

```python
student = {"name": "Maya", "grade": 10}
print(student["Name"])   # Maya
```

[Solution 5.9.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-9-1) &middot; [`ex_5_9_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_9_1.py)

### Exercise 5.9.2 — Updating a grade
{: #ex-5-9-2 }

The program should change the grade to 11 and print 11.

```python
student = {"name": "Maya", "grade": 10}
student("grade") = 11
print(student["grade"])   # 11
```

[Solution 5.9.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-9-2) &middot; [`ex_5_9_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_9_2.py)

### Exercise 5.9.3 — Missing key
{: #ex-5-9-3 }

The program should safely look up a missing subject and print "not found" instead of crashing.

```python
student = {"name": "Maya", "grade": 10}
subject = student["favorite_subject"]
print(subject)   # not found
```

[Solution 5.9.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-9-3) &middot; [`ex_5_9_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_9_3.py)

### Exercise 5.9.4 — Safe default with get
{: #ex-5-9-4 }

Using `.get`, the program should print "science" when the key exists.

```python
student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(Subject)   # science
```

[Solution 5.9.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-9-4) &middot; [`ex_5_9_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_9_4.py)

### Exercise 5.9.5 — Adding an entry
{: #ex-5-9-5 }

The program should add a phone number to the contact and print it.

```python
contact = {"name": "Leo"}
contact["phone"] == "555-0100"
print(contact["phone"])   # 555-0100
```

[Solution 5.9.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-9-5) &middot; [`ex_5_9_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_9_5.py)

## Variables and Types

### Exercise 5.10.1 — Reading a number
{: #ex-5-10-1 }

Input arrives as text. The program should turn "25" into a number and print 30 after adding 5.

```python
age_text = "25"
age = age_text + 5
print(age)   # 30
```

[Solution 5.10.1]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-10-1) &middot; [`ex_5_10_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_10_1.py)

### Exercise 5.10.2 — Building a message
{: #ex-5-10-2 }

The program should combine a label and a number into one sentence: "Score: 90".

```python
score = 90
message = "Score: " + score
print(message)   # Score: 90
```

[Solution 5.10.2]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-10-2) &middot; [`ex_5_10_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_10_2.py)

### Exercise 5.10.3 — Checking a type
{: #ex-5-10-3 }

The program should report the type of a price as `float`.

```python
price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == int)   # expected: True
```

[Solution 5.10.3]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-10-3) &middot; [`ex_5_10_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_10_3.py)

### Exercise 5.10.4 — Converting to float
{: #ex-5-10-4 }

The program should turn the text "2.5" into a float and print double it, 5.0.

```python
weight_text = "2.5"
weight = int(weight_text)
print(weight * 2)   # 5.0
```

[Solution 5.10.4]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-10-4) &middot; [`ex_5_10_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_10_4.py)

### Exercise 5.10.5 — Whole-number average
{: #ex-5-10-5 }

Two test scores are 80 and 91. The program should print their average as a whole number, 85.

```python
score1 = 80
score2 = 91

average = str((score1 + score2) / 2)
print(int(average))   # 85
```

[Solution 5.10.5]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-10-5) &middot; [`ex_5_10_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_5_10_5.py)

