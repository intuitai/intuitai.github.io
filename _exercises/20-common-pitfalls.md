---
title: "Chapter 20: Common Pitfalls"
short_title: "Ch. 20 — Common Pitfalls"
layout: post
permalink: /ep/exercises/20-common-pitfalls/
order: 12
chapter: 20
exercise_count: 130
---

130 *Find the Bug* exercises from Chapter 20 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 20 solutions]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 20.1.1–20.1.5

### Exercise 20.1.1 — Missing colon after `if`
{: #ex-20-1-1 }

This program should print `"Fever"` when a temperature is at or above 38 degrees Celsius.

```python
temperature = 39
if temperature >= 38
    print("Fever")
```

[Solution 20.1.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-1-1) &middot; [`ex_20_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_1_1.py)

### Exercise 20.1.2 — Missing colon after `for`
{: #ex-20-1-2 }

This program should print each planet's distance from the Sun in millions of kilometers.

```python
distances = [58, 108, 150]
for distance in distances
    print(distance)
```

[Solution 20.1.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-1-2) &middot; [`ex_20_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_1_2.py)

### Exercise 20.1.3 — Missing colon after `while`
{: #ex-20-1-3 }

This program should count down from 3 to 1 for a rocket launch.

```python
seconds = 3
while seconds > 0
    print(seconds)
    seconds = seconds - 1
```

[Solution 20.1.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-1-3) &middot; [`ex_20_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_1_3.py)

### Exercise 20.1.4 — Missing colon after `def`
{: #ex-20-1-4 }

This program should define a function that returns the area of a rectangle and print it.

```python
def rectangle_area(width, height)
    return width * height

print(rectangle_area(4, 5))  # 20
```

[Solution 20.1.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-1-4) &middot; [`ex_20_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_1_4.py)

### Exercise 20.1.5 — Missing colon after `elif`
{: #ex-20-1-5 }

This program should label a test score as a pass, a borderline, or a fail.

```python
score = 55
if score >= 60:
    print("Pass")
elif score >= 50
    print("Borderline")
else:
    print("Fail")
```

[Solution 20.1.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-1-5) &middot; [`ex_20_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_1_5.py)

## Exercises 20.2.1–20.2.5

### Exercise 20.2.1 — Body not indented
{: #ex-20-2-1 }

This program should greet a registered member.

```python
member = "Alex"
if member == "Alex":
print("Welcome back")
```

[Solution 20.2.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-2-1) &middot; [`ex_20_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_2_1.py)

### Exercise 20.2.2 — Inconsistent indentation in a loop
{: #ex-20-2-2 }

This program should add up the rainfall for three days.

```python
rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
      print(total)  # 35
```

[Solution 20.2.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-2-2) &middot; [`ex_20_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_2_2.py)

### Exercise 20.2.3 — Function body not indented
{: #ex-20-2-3 }

This program should return the perimeter of a square and print it.

```python
def square_perimeter(side):
return 4 * side

print(square_perimeter(6))  # 24
```

[Solution 20.2.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-2-3) &middot; [`ex_20_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_2_3.py)

### Exercise 20.2.4 — Over-indented statement
{: #ex-20-2-4 }

This program should print whether water is boiling at the given temperature.

```python
temperature = 100
if temperature >= 100:
        print("Boiling")
    print("Done checking")
```

[Solution 20.2.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-2-4) &middot; [`ex_20_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_2_4.py)

### Exercise 20.2.5 — Indentation mixing two blocks
{: #ex-20-2-5 }

This program should print each grade and then announce the report is finished.

```python
grades = [88, 91, 79]
for grade in grades:
    print(grade)
  print("Report complete")
```

[Solution 20.2.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-2-5) &middot; [`ex_20_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_2_5.py)

## Exercises 20.3.1–20.3.5

### Exercise 20.3.1 — Assignment inside an `if`
{: #ex-20-3-1 }

This program should check whether a thermostat is set to 20 degrees.

```python
thermostat = 20
if thermostat = 20:
    print("Comfortable")
```

[Solution 20.3.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-3-1) &middot; [`ex_20_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_3_1.py)

### Exercise 20.3.2 — Assignment when comparing a password length
{: #ex-20-3-2 }

This program should confirm a password has exactly 8 characters.

```python
length = 8
if length = 8:
    print("Valid length")
```

[Solution 20.3.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-3-2) &middot; [`ex_20_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_3_2.py)

### Exercise 20.3.3 — Equality used where assignment is meant
{: #ex-20-3-3 }

This program should set a starting balance and print it.

```python
balance == 100
print(balance)  # 100
```

[Solution 20.3.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-3-3) &middot; [`ex_20_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_3_3.py)

### Exercise 20.3.4 — Assignment inside a `while`
{: #ex-20-3-4 }

This program should keep doubling a sample count until it reaches at least 50.

```python
count = 5
while count = count * 2:
    print(count)
```

[Solution 20.3.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-3-4) &middot; [`ex_20_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_3_4.py)

### Exercise 20.3.5 — Equality used for assignment
{: #ex-20-3-5 }

This program should record a measured speed and print it in km/h.

```python
speed == 60
print("Speed:", speed)  # Speed: 60
```

[Solution 20.3.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-3-5) &middot; [`ex_20_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_3_5.py)

## Exercises 20.4.1–20.4.5

### Exercise 20.4.1 — Printing before assigning
{: #ex-20-4-1 }

This program should report the number of students in a class.

```python
print(students)
students = 30
```

[Solution 20.4.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-4-1) &middot; [`ex_20_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_4_1.py)

### Exercise 20.4.2 — Using a sum before it exists
{: #ex-20-4-2 }

This program should add the first two test marks together.

```python
first = 70
second = 85
print(total)
total = first + second
```

[Solution 20.4.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-4-2) &middot; [`ex_20_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_4_2.py)

### Exercise 20.4.3 — Using a result before computing it
{: #ex-20-4-3 }

This program should compute and print the area of a circle with radius 3.

```python
radius = 3
print(area)
area = 3.14159 * radius * radius
```

[Solution 20.4.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-4-3) &middot; [`ex_20_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_4_3.py)

### Exercise 20.4.4 — Reading a counter that is set later
{: #ex-20-4-4 }

This program should print how many laps a runner completed.

```python
print("Laps:", laps)
laps = 4
```

[Solution 20.4.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-4-4) &middot; [`ex_20_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_4_4.py)

### Exercise 20.4.5 — Using a price before defining it
{: #ex-20-4-5 }

This program should print the total cost of 3 notebooks.

```python
quantity = 3
print(quantity * price)
price = 2
```

[Solution 20.4.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-4-5) &middot; [`ex_20_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_4_5.py)

## Exercises 20.5.1–20.5.5

### Exercise 20.5.1 — Misspelled variable in a print
{: #ex-20-5-1 }

This program should print a welcome message.

```python
greeting = "Good morning"
print(greting)
```

[Solution 20.5.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-5-1) &middot; [`ex_20_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_5_1.py)

### Exercise 20.5.2 — Misspelled variable in a calculation
{: #ex-20-5-2 }

This program should print the distance traveled at 60 km/h for 2 hours.

```python
speed = 60
hours = 2
distance = sped * hours
print(distance)  # 120
```

[Solution 20.5.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-5-2) &middot; [`ex_20_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_5_2.py)

### Exercise 20.5.3 — Inconsistent capitalization
{: #ex-20-5-3 }

This program should print a city's recorded high temperature.

```python
Temperature = 31
print(temperature)
```

[Solution 20.5.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-5-3) &middot; [`ex_20_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_5_3.py)

### Exercise 20.5.4 — Misspelled variable when updating
{: #ex-20-5-4 }

This program should add a tip to a restaurant bill and print the total.

```python
bill = 40
tip = 6
total = bil + tip
print(total)  # 46
```

[Solution 20.5.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-5-4) &middot; [`ex_20_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_5_4.py)

### Exercise 20.5.5 — Misspelled list name
{: #ex-20-5-5 }

This program should print the average of three exam scores.

```python
scores = [80, 90, 100]
average = sum(score) / len(scores)
print(average)  # 90.0
```

[Solution 20.5.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-5-5) &middot; [`ex_20_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_5_5.py)

## Exercises 20.6.1–20.6.5

### Exercise 20.6.1 — Joining text and a number
{: #ex-20-6-1 }

This program should print a label with the day's step count.

```python
steps = 8000
print("Steps today: " + steps)
```

[Solution 20.6.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-6-1) &middot; [`ex_20_6_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_6_1.py)

### Exercise 20.6.2 — Adding a number to a string label
{: #ex-20-6-2 }

This program should print how many liters of water to drink.

```python
liters = 2
print("Drink " + liters + " liters")
```

[Solution 20.6.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-6-2) &middot; [`ex_20_6_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_6_2.py)

### Exercise 20.6.3 — Concatenating a price into a message
{: #ex-20-6-3 }

This program should announce the ticket price.

```python
price = 15
message = "Ticket costs $" + price
print(message)
```

[Solution 20.6.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-6-3) &middot; [`ex_20_6_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_6_3.py)

### Exercise 20.6.4 — Combining a count with text
{: #ex-20-6-4 }

This program should report how many books are on a shelf.

```python
books = 12
print(books + " books on the shelf")
```

[Solution 20.6.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-6-4) &middot; [`ex_20_6_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_6_4.py)

### Exercise 20.6.5 — Treating a string as a number
{: #ex-20-6-5 }

This program should add a bonus of 10 points to a stored score.

```python
score = "75"
print(score + 10)
```

[Solution 20.6.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-6-5) &middot; [`ex_20_6_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_6_5.py)

## Exercises 20.7.1–20.7.5

### Exercise 20.7.1 — Adding to raw input
{: #ex-20-7-1 }

This program should ask for a year and print the next year.

```python
year = input("Enter the year: ")
print(year + 1)
```

[Solution 20.7.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-7-1) &middot; [`ex_20_7_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_7_1.py)

### Exercise 20.7.2 — Doubling a typed quantity
{: #ex-20-7-2 }

This program should double the number of cookies the user enters.

```python
cookies = input("How many cookies? ")
print(cookies * 2 == 24)  # for input 12
```

[Solution 20.7.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-7-2) &middot; [`ex_20_7_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_7_2.py)

### Exercise 20.7.3 — Summing two typed numbers
{: #ex-20-7-3 }

This program should add two typed prices and print the total.

```python
first = int(input("First price: "))
second = input("Second price: ")
print(first + second)
```

[Solution 20.7.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-7-3) &middot; [`ex_20_7_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_7_3.py)

### Exercise 20.7.4 — Comparing typed age to a limit
{: #ex-20-7-4 }

This program should print `"Adult"` when the typed age is at least 18.

```python
age = input("Your age: ")
if age >= 18:
    print("Adult")
```

[Solution 20.7.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-7-4) &middot; [`ex_20_7_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_7_4.py)

### Exercise 20.7.5 — Averaging a typed temperature
{: #ex-20-7-5 }

This program should halve the temperature the user types.

```python
temperature = input("Temperature: ")
print(temperature / 2)
```

[Solution 20.7.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-7-5) &middot; [`ex_20_7_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_7_5.py)

## Exercises 20.8.1–20.8.5

### Exercise 20.8.1 — Splitting students into teams
{: #ex-20-8-1 }

This program should print how many full teams of 4 can be made from 30 students.

```python
students = 30
team_size = 4
print(students / team_size)  # 7
```

[Solution 20.8.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-8-1) &middot; [`ex_20_8_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_8_1.py)

### Exercise 20.8.2 — Pages per chapter
{: #ex-20-8-2 }

This program should print how many whole pages each of 5 chapters gets from 52 pages.

```python
pages = 52
chapters = 5
print(pages / chapters)  # 10
```

[Solution 20.8.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-8-2) &middot; [`ex_20_8_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_8_2.py)

### Exercise 20.8.3 — Counting full boxes
{: #ex-20-8-3 }

This program should print how many full boxes of 6 eggs come from 40 eggs.

```python
eggs = 40
per_box = 6
full_boxes = eggs / per_box
print(full_boxes)  # 6
```

[Solution 20.8.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-8-3) &middot; [`ex_20_8_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_8_3.py)

### Exercise 20.8.4 — Whole minutes from seconds
{: #ex-20-8-4 }

This program should print the number of whole minutes in 200 seconds.

```python
seconds = 200
minutes = seconds / 60
print(minutes)  # 3
```

[Solution 20.8.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-8-4) &middot; [`ex_20_8_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_8_4.py)

### Exercise 20.8.5 — Sharing marbles evenly
{: #ex-20-8-5 }

This program should print how many marbles each of 3 children gets from 25 marbles.

```python
marbles = 25
children = 3
print(marbles / children)  # 8
```

[Solution 20.8.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-8-5) &middot; [`ex_20_8_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_8_5.py)

## Exercises 20.9.1–20.9.5

### Exercise 20.9.1 — Area of a square
{: #ex-20-9-1 }

This program should print the area of a square with side 5 (side squared).

```python
side = 5
print(side ^ 2)  # 25
```

[Solution 20.9.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-9-1) &middot; [`ex_20_9_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_9_1.py)

### Exercise 20.9.2 — Cube of a number
{: #ex-20-9-2 }

This program should print 4 raised to the third power.

```python
base = 4
print(base ^ 3)  # 64
```

[Solution 20.9.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-9-2) &middot; [`ex_20_9_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_9_2.py)

### Exercise 20.9.3 — Compound growth
{: #ex-20-9-3 }

This program should print 2 raised to the tenth power.

```python
print(2 ^ 10)  # 1024
```

[Solution 20.9.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-9-3) &middot; [`ex_20_9_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_9_3.py)

### Exercise 20.9.4 — Volume of a cube
{: #ex-20-9-4 }

This program should print the volume of a cube with edge 3 (edge cubed).

```python
edge = 3
volume = edge ^ 3
print(volume)  # 27
```

[Solution 20.9.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-9-4) &middot; [`ex_20_9_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_9_4.py)

### Exercise 20.9.5 — Energy term squared
{: #ex-20-9-5 }

This program should print the speed squared for a kinetic-energy calculation.

```python
speed = 6
print(speed ^ 2)  # 36
```

[Solution 20.9.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-9-5) &middot; [`ex_20_9_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_9_5.py)

## Exercises 20.10.1–20.10.5

### Exercise 20.10.1 — Setting a fourth temperature
{: #ex-20-10-1 }

This program should replace a placeholder list with three real readings, then store a fourth.

```python
readings = [20, 22, 21]
readings[3] = 23
print(readings)
```

[Solution 20.10.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-10-1) &middot; [`ex_20_10_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_10_1.py)

### Exercise 20.10.2 — Recording a new score
{: #ex-20-10-2 }

This program should store a new game score after the existing three.

```python
scores = [10, 15, 20]
scores[3] = 25
print(scores)
```

[Solution 20.10.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-10-2) &middot; [`ex_20_10_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_10_2.py)

### Exercise 20.10.3 — Filling in a weekly total
{: #ex-20-10-3 }

This program should set the fourth week's sales figure.

```python
weekly_sales = [100, 120, 90]
weekly_sales[3] = 110
print(weekly_sales)
```

[Solution 20.10.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-10-3) &middot; [`ex_20_10_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_10_3.py)

### Exercise 20.10.4 — Adding a fourth runner's time
{: #ex-20-10-4 }

This program should store a fourth lap time at the next position.

```python
lap_times = [45, 47, 44]
lap_times[len(lap_times)] = 46
print(lap_times)
```

[Solution 20.10.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-10-4) &middot; [`ex_20_10_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_10_4.py)

### Exercise 20.10.5 — Appending a measurement
{: #ex-20-10-5 }

This program should add one more pH reading to the list.

```python
ph_values = [7.0, 6.8, 7.2]
ph_values[3] = 6.9
print(ph_values)
```

[Solution 20.10.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-10-5) &middot; [`ex_20_10_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_10_5.py)

## Exercises 20.11.1–20.11.5

### Exercise 20.11.1 — Reading the last color
{: #ex-20-11-1 }

This program should print the last color in the list.

```python
colors = ["red", "green", "blue"]
print(colors[3])
```

[Solution 20.11.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-11-1) &middot; [`ex_20_11_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_11_1.py)

### Exercise 20.11.2 — Printing each day's high
{: #ex-20-11-2 }

This program should print all four recorded high temperatures.

```python
highs = [28, 30, 29, 31]
for i in range(5):
    print(highs[i])
```

[Solution 20.11.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-11-2) &middot; [`ex_20_11_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_11_2.py)

### Exercise 20.11.3 — Showing the third prize
{: #ex-20-11-3 }

This program should print the third prize from the list.

```python
prizes = ["gold", "silver"]
print(prizes[2])
```

[Solution 20.11.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-11-3) &middot; [`ex_20_11_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_11_3.py)

### Exercise 20.11.4 — Last item by length
{: #ex-20-11-4 }

This program should print the last student's name in the list.

```python
students = ["Mia", "Noah", "Liam"]
print(students[len(students)])
```

[Solution 20.11.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-11-4) &middot; [`ex_20_11_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_11_4.py)

### Exercise 20.11.5 — Looping one step too far
{: #ex-20-11-5 }

This program should print every price in the list.

```python
prices = [3, 5, 9]
index = 0
while index <= len(prices):
    print(prices[index])
    index = index + 1
```

[Solution 20.11.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-11-5) &middot; [`ex_20_11_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_11_5.py)

## Exercises 20.12.1–20.12.5

### Exercise 20.12.1 — Building a shopping list
{: #ex-20-12-1 }

This program should make a list of groceries and add one more item.

```python
groceries = ("milk", "bread", "eggs")
groceries.append("butter")
print(groceries)
```

[Solution 20.12.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-12-1) &middot; [`ex_20_12_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_12_1.py)

### Exercise 20.12.2 — Collecting daily steps
{: #ex-20-12-2 }

This program should create a list of step counts and add today's count.

```python
steps = (8000, 9500, 7000)
steps.append(10000)
print(steps)
```

[Solution 20.12.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-12-2) &middot; [`ex_20_12_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_12_2.py)

### Exercise 20.12.3 — A list of temperatures
{: #ex-20-12-3 }

This program should change the first temperature reading to 19.

```python
temperatures = (21, 22, 20)
temperatures[0] = 19
print(temperatures)
```

[Solution 20.12.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-12-3) &middot; [`ex_20_12_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_12_3.py)

### Exercise 20.12.4 — Listing class names
{: #ex-20-12-4 }

This program should build a list of subjects and add one more.

```python
subjects = ("Math", "Science")
subjects.append("History")
print(subjects)
```

[Solution 20.12.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-12-4) &middot; [`ex_20_12_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_12_4.py)

### Exercise 20.12.5 — A list of scores to extend
{: #ex-20-12-5 }

This program should start a list of scores and append a new one.

```python
scores = (88, 92)
scores.append(75)
print(scores)
```

[Solution 20.12.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-12-5) &middot; [`ex_20_12_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_12_5.py)

## Exercises 20.13.1–20.13.5

### Exercise 20.13.1 — Capitalizing a name
{: #ex-20-13-1 }

This program should change the first letter of a name to a capital `"S"`.

```python
name = "sam"
name[0] = "S"
print(name)
```

[Solution 20.13.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-13-1) &middot; [`ex_20_13_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_13_1.py)

### Exercise 20.13.2 — Fixing a typo in a word
{: #ex-20-13-2 }

This program should change `"hpllo"` into `"hello"` by replacing one letter.

```python
word = "hpllo"
word[1] = "e"
print(word)
```

[Solution 20.13.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-13-2) &middot; [`ex_20_13_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_13_2.py)

### Exercise 20.13.3 — Replacing a digit in a code
{: #ex-20-13-3 }

This program should change the first character of a code to `"9"`.

```python
code = "12345"
code[0] = "9"
print(code)
```

[Solution 20.13.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-13-3) &middot; [`ex_20_13_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_13_3.py)

### Exercise 20.13.4 — Masking a letter
{: #ex-20-13-4 }

This program should hide the last letter of a word with an asterisk.

```python
secret = "open"
secret[3] = "*"
print(secret)
```

[Solution 20.13.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-13-4) &middot; [`ex_20_13_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_13_4.py)

### Exercise 20.13.5 — Correcting a unit label
{: #ex-20-13-5 }

This program should change the first letter of `"km"` to make `"Km"`.

```python
unit = "km"
unit[0] = "K"
print(unit)
```

[Solution 20.13.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-13-5) &middot; [`ex_20_13_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_13_5.py)

## Exercises 20.14.1–20.14.5

### Exercise 20.14.1 — Checking a student's full name
{: #ex-20-14-1 }

This program should announce a match when the typed name equals the enrolled name.

```python
enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name is enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
```

[Solution 20.14.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-14-1) &middot; [`ex_20_14_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_14_1.py)

### Exercise 20.14.2 — Matching a password phrase
{: #ex-20-14-2 }

The program should grant access when the typed phrase equals the stored phrase.

```python
stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase is stored_phrase:
    print("Access granted")
else:
    print("Access denied")
```

[Solution 20.14.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-14-2) &middot; [`ex_20_14_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_14_2.py)

### Exercise 20.14.3 — Confirming a recipe title
{: #ex-20-14-3 }

A recipe title is built from its words and should match the saved title.

```python
saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title is saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
```

[Solution 20.14.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-14-3) &middot; [`ex_20_14_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_14_3.py)

### Exercise 20.14.4 — Comparing two shopping lists
{: #ex-20-14-4 }

The program should report that two grocery lists hold the same items.

```python
cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one is cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
```

[Solution 20.14.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-14-4) &middot; [`ex_20_14_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_14_4.py)

### Exercise 20.14.5 — Verifying a reading list
{: #ex-20-14-5 }

The program checks whether the books read so far match the planned reading list.

```python
planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far is planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
```

[Solution 20.14.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-14-5) &middot; [`ex_20_14_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_14_5.py)

## Exercises 20.15.1–20.15.5

### Exercise 20.15.1 — Reading the current temperature
{: #ex-20-15-1 }

This program should print the temperature returned by the function.

```python
def current_temperature():
    return 21.5

print("Temperature:", current_temperature)
```

[Solution 20.15.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-15-1) &middot; [`ex_20_15_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_15_1.py)

### Exercise 20.15.2 — Counting words in a sentence
{: #ex-20-15-2 }

The program should report how many words a sentence contains.

```python
def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count)
```

[Solution 20.15.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-15-2) &middot; [`ex_20_15_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_15_2.py)

### Exercise 20.15.3 — Rolling for a starting number
{: #ex-20-15-3 }

The program should print a fixed starting score produced by a helper.

```python
def starting_score():
    return 100

score = starting_score
print("You begin with", score, "points")
```

[Solution 20.15.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-15-3) &middot; [`ex_20_15_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_15_3.py)

### Exercise 20.15.4 — Area of a circle
{: #ex-20-15-4 }

This program should compute and print the area of a circle with radius 4.

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area / 2)
```

[Solution 20.15.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-15-4) &middot; [`ex_20_15_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_15_4.py)

### Exercise 20.15.5 — Greeting the next runner
{: #ex-20-15-5 }

The program should print a greeting for the runner.

```python
def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner
print(message)
```

[Solution 20.15.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-15-5) &middot; [`ex_20_15_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_15_5.py)

## Exercises 20.16.1–20.16.5

### Exercise 20.16.1 — Converting miles to kilometers
{: #ex-20-16-1 }

This program should print the distance in kilometers for 5 miles.

```python
def miles_to_km(miles):
    km = miles * 1.60934

print("Kilometers:", miles_to_km(5))
```

[Solution 20.16.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-16-1) &middot; [`ex_20_16_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_16_1.py)

### Exercise 20.16.2 — Averaging three test grades
{: #ex-20-16-2 }

The program should print the average of three grades.

```python
def average(a, b, c):
    total = a + b + c
    average_value = total / 3

print("Average:", average(80, 90, 100))
```

[Solution 20.16.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-16-2) &middot; [`ex_20_16_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_16_2.py)

### Exercise 20.16.3 — Doubling a recipe
{: #ex-20-16-3 }

This program should return the doubled amount of flour.

```python
def double_amount(cups):
    doubled = cups * 2

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
```

[Solution 20.16.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-16-3) &middot; [`ex_20_16_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_16_3.py)

### Exercise 20.16.4 — Perimeter of a rectangle
{: #ex-20-16-4 }

The program should print the perimeter of a 6 by 4 rectangle.

```python
def perimeter(length, width):
    p = 2 * (length + width)

print("Perimeter:", perimeter(6, 4))
```

[Solution 20.16.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-16-4) &middot; [`ex_20_16_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_16_4.py)

### Exercise 20.16.5 — Tax on a purchase
{: #ex-20-16-5 }

This program should return the tax owed on a $200 purchase at 8 percent.

```python
def tax_owed(price, rate):
    tax = price * rate / 100

print("Tax:", tax_owed(200, 8))
```

[Solution 20.16.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-16-5) &middot; [`ex_20_16_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_16_5.py)

## Exercises 20.17.1–20.17.5

### Exercise 20.17.1 — Tallying rainfall
{: #ex-20-17-1 }

The program should add today's rainfall to the running total and print it.

```python
total_rain = 0.0

def add_rain(today):
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
```

[Solution 20.17.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-17-1) &middot; [`ex_20_17_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_17_1.py)

### Exercise 20.17.2 — Keeping a running balance
{: #ex-20-17-2 }

This program should subtract a withdrawal from the account balance.

```python
balance = 500

def withdraw(amount):
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
```

[Solution 20.17.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-17-2) &middot; [`ex_20_17_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_17_2.py)

### Exercise 20.17.3 — Counting visitors
{: #ex-20-17-3 }

The program should increase the visitor count by one each time someone enters.

```python
visitors = 0

def enter():
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
```

[Solution 20.17.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-17-3) &middot; [`ex_20_17_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_17_3.py)

### Exercise 20.17.4 — Accumulating distance
{: #ex-20-17-4 }

This program should add a new leg of a trip to the total distance traveled.

```python
distance_km = 0

def drive(leg):
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
```

[Solution 20.17.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-17-4) &middot; [`ex_20_17_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_17_4.py)

### Exercise 20.17.5 — Building a points streak
{: #ex-20-17-5 }

The program should multiply the current streak by 2 each round.

```python
streak = 1

def double_streak():
    streak = streak * 2

double_streak()
print("Streak:", streak)
```

[Solution 20.17.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-17-5) &middot; [`ex_20_17_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_17_5.py)

## Exercises 20.18.1–20.18.5

### Exercise 20.18.1 — Saving a shopping list
{: #ex-20-18-1 }

This program should write the shopping list to a file and leave no file handle open.

```python
groceries = "milk\neggs\nbread\n"
list_file = open("groceries.txt", "w")
list_file.write(groceries)
print("Shopping list saved")
```

[Solution 20.18.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-18-1) &middot; [`ex_20_18_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_18_1.py)

### Exercise 20.18.2 — Logging a temperature reading
{: #ex-20-18-2 }

The program should append one temperature reading to a log file safely.

```python
log = open("temps.txt", "a")
log.write("21.5\n")
```

[Solution 20.18.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-18-2) &middot; [`ex_20_18_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_18_2.py)

### Exercise 20.18.3 — Recording a high score
{: #ex-20-18-3 }

This program should save the player's high score to disk safely.

```python
high_score = 4200
score_file = open("highscore.txt", "w")
score_file.write(str(high_score))
print("High score recorded")
```

[Solution 20.18.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-18-3) &middot; [`ex_20_18_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_18_3.py)

### Exercise 20.18.4 — Writing a daily journal entry
{: #ex-20-18-4 }

The program should write one journal line to a file safely.

```python
entry = "Today I walked 10000 steps.\n"
journal = open("journal.txt", "w")
journal.write(entry)
print("Entry written")
```

[Solution 20.18.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-18-4) &middot; [`ex_20_18_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_18_4.py)

### Exercise 20.18.5 — Storing a measured weight
{: #ex-20-18-5 }

This program should save a measured weight in kilograms to a file safely.

```python
weight_kg = 72.4
weight_file = open("weight.txt", "w")
weight_file.write(f"{weight_kg}\n")
```

[Solution 20.18.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-18-5) &middot; [`ex_20_18_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_18_5.py)

## Exercises 20.19.1–20.19.5

### Exercise 20.19.1 — Converting a typed age
{: #ex-20-19-1 }

This program should turn typed text into a number and warn only when the text is not a number.

```python
text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except:
    print("Please type a whole number")
```

[Solution 20.19.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-19-1) &middot; [`ex_20_19_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_19_1.py)

### Exercise 20.19.2 — Dividing a bill among friends
{: #ex-20-19-2 }

The program should split a bill and report only when the number of people is zero.

```python
bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except:
    print("There must be at least one person")
```

[Solution 20.19.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-19-2) &middot; [`ex_20_19_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_19_2.py)

### Exercise 20.19.3 — Looking up a price
{: #ex-20-19-3 }

This program should read a price from a dictionary and warn only when the item is missing.

```python
prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except:
    print("That item is not on the price list")
```

[Solution 20.19.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-19-3) &middot; [`ex_20_19_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_19_3.py)

### Exercise 20.19.4 — Parsing a temperature
{: #ex-20-19-4 }

The program should convert typed text to a float and warn only on bad number text.

```python
reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except:
    print("That is not a valid temperature")
```

[Solution 20.19.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-19-4) &middot; [`ex_20_19_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_19_4.py)

### Exercise 20.19.5 — Reading a list position
{: #ex-20-19-5 }

This program should print the third score and warn only when the position is out of range.

```python
scores = [88, 92]
try:
    print("Third score:", scores[2])
except:
    print("There is no score at that position")
```

[Solution 20.19.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-19-5) &middot; [`ex_20_19_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_19_5.py)

## Exercises 20.20.1–20.20.5

### Exercise 20.20.1 — Accepting a yes answer
{: #ex-20-20-1 }

This program should accept the answer "yes" no matter how it is capitalized.

```python
answer = "YES"
if answer == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
```

[Solution 20.20.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-20-1) &middot; [`ex_20_20_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_20_1.py)

### Exercise 20.20.2 — Matching a chosen color
{: #ex-20-20-2 }

The program should detect the favorite color "blue" regardless of case.

```python
favorite = "Blue"
if favorite.upper() == "blue":
    print("You picked blue")
```

[Solution 20.20.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-20-2) &middot; [`ex_20_20_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_20_2.py)

### Exercise 20.20.3 — Checking a chemical symbol
{: #ex-20-20-3 }

This program should recognize the element symbol "Na" however the user types it.

```python
symbol = "NA"
if symbol == "Na":
    print("That is sodium")
```

[Solution 20.20.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-20-3) &middot; [`ex_20_20_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_20_3.py)

### Exercise 20.20.4 — Looking up a city name
{: #ex-20-20-4 }

The program should find "Paris" in the list even if typed in lowercase.

```python
cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in cities:
    print("City found")
else:
    print("City not found")
```

[Solution 20.20.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-20-4) &middot; [`ex_20_20_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_20_4.py)

### Exercise 20.20.5 — Confirming a unit
{: #ex-20-20-5 }

This program should accept the unit "kg" whether typed as "KG", "Kg", or "kg".

```python
unit = "KG"
if unit.upper() == "kg":
    print("Kilograms")
```

[Solution 20.20.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-20-5) &middot; [`ex_20_20_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_20_5.py)

## Exercises 20.21.1–20.21.5

### Exercise 20.21.1 — Printing each planet
{: #ex-20-21-1 }

This program should print every planet name on its own line.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
for i in range(len(planets)):
    print(planet)
```

[Solution 20.21.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-21-1) &middot; [`ex_20_21_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_21_1.py)

### Exercise 20.21.2 — Summing daily sales
{: #ex-20-21-2 }

The program should add up every day's sales and print the total.

```python
sales = [120, 85, 200, 95]
total = 0
for i in range(len(sales)):
    total = total + sales
print("Total sales:", total)
```

[Solution 20.21.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-21-2) &middot; [`ex_20_21_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_21_2.py)

### Exercise 20.21.3 — Greeting each guest
{: #ex-20-21-3 }

This program should print a greeting for every guest.

```python
guests = ["Ana", "Ben", "Cara"]
for guest in range(len(guests)):
    print("Welcome,", guest)
```

[Solution 20.21.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-21-3) &middot; [`ex_20_21_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_21_3.py)

### Exercise 20.21.4 — Doubling each measurement
{: #ex-20-21-4 }

The program should print double each measurement in the list.

```python
measurements = [3, 5, 8]
for m in range(len(measurements)):
    print(m * 2)
```

[Solution 20.21.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-21-4) &middot; [`ex_20_21_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_21_4.py)

### Exercise 20.21.5 — Listing the ingredients
{: #ex-20-21-5 }

This program should print each ingredient.

```python
ingredients = ["flour", "sugar", "butter"]
for item in range(len(ingredients)):
    print(item)
```

[Solution 20.21.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-21-5) &middot; [`ex_20_21_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_21_5.py)

## Exercises 20.22.1–20.22.5

### Exercise 20.22.1 — Counting items in a basket
{: #ex-20-22-1 }

This program should count the letters in a fruit name after storing some numbers.

```python
len = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
```

[Solution 20.22.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-22-1) &middot; [`ex_20_22_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_22_1.py)

### Exercise 20.22.2 — Totaling a receipt
{: #ex-20-22-2 }

The program should add up the prices on a receipt.

```python
sum = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
```

[Solution 20.22.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-22-2) &middot; [`ex_20_22_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_22_2.py)

### Exercise 20.22.3 — Turning a word into letters
{: #ex-20-22-3 }

This program should turn the word into a list of its letters.

```python
list = "abc"
letters = list("hello")
print(letters)
```

[Solution 20.22.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-22-3) &middot; [`ex_20_22_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_22_3.py)

### Exercise 20.22.4 — Labeling a measurement
{: #ex-20-22-4 }

The program should print a number alongside its unit as text.

```python
str = "kilograms"
weight = 70
print(str(weight) + " " + str)
```

[Solution 20.22.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-22-4) &middot; [`ex_20_22_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_22_4.py)

### Exercise 20.22.5 — Finding the largest reading
{: #ex-20-22-5 }

This program should print the largest of three sensor readings.

```python
max = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
```

[Solution 20.22.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-22-5) &middot; [`ex_20_22_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_22_5.py)

## Exercises 20.23.1–20.23.5

### Exercise 20.23.1 — Splitting a bill exactly
{: #ex-20-23-1 }

This program should confirm that three shares of $0.10 add up to $0.30.

```python
share = 0.10
total = share + share + share
if total == 0.30:
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
```

[Solution 20.23.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-23-1) &middot; [`ex_20_23_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_23_1.py)

### Exercise 20.23.2 — Adding two distances
{: #ex-20-23-2 }

The program should confirm that 0.1 km plus 0.2 km equals 0.3 km.

```python
leg_one = 0.1
leg_two = 0.2
if leg_one + leg_two == 0.3:
    print("Distances match")
else:
    print("Distances do not match")
```

[Solution 20.23.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-23-2) &middot; [`ex_20_23_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_23_2.py)

### Exercise 20.23.3 — Checking a measured volume
{: #ex-20-23-3 }

This program should confirm that three 0.1 L pours fill a 0.3 L cup.

```python
pour = 0.1
filled = pour * 3
if filled == 0.3:
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
```

[Solution 20.23.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-23-3) &middot; [`ex_20_23_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_23_3.py)

### Exercise 20.23.4 — Verifying a percentage
{: #ex-20-23-4 }

The program should check that 0.7 plus 0.1 equals 0.8.

```python
part_one = 0.7
part_two = 0.1
if part_one + part_two == 0.8:
    print("Percentages add correctly")
else:
    print("Percentages do not add correctly")
```

[Solution 20.23.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-23-4) &middot; [`ex_20_23_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_23_4.py)

### Exercise 20.23.5 — Comparing a savings target
{: #ex-20-23-5 }

This program should confirm that saving $1.10 three times reaches $3.30.

```python
weekly = 1.10
saved = weekly * 3
if saved == 3.30:
    print("You reached the target")
else:
    print("You did not reach the target")
```

[Solution 20.23.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-23-5) &middot; [`ex_20_23_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_23_5.py)

## Exercises 20.24.1–20.24.5

### Exercise 20.24.1 — Average speed of a trip
{: #ex-20-24-1 }

This program should compute average speed (distance over time) for a 150 km trip in 3 hours and print 50.0.

```python
def average_speed(distance, time):
    return time / distance

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
```

[Solution 20.24.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-24-1) &middot; [`ex_20_24_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_24_1.py)

### Exercise 20.24.2 — Final price after discount
{: #ex-20-24-2 }

The program should subtract a 20 percent discount from a $50 item and print 40.0.

```python
def final_price(price, percent_off):
    discount = price * percent_off
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
```

[Solution 20.24.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-24-2) &middot; [`ex_20_24_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_24_2.py)

### Exercise 20.24.3 — Kinetic energy of a moving cart
{: #ex-20-24-3 }

This program should compute kinetic energy (one-half m v squared) for m=2, v=3 and print 9.0.

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed * 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
```

[Solution 20.24.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-24-3) &middot; [`ex_20_24_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_24_3.py)

### Exercise 20.24.4 — Celsius to Fahrenheit
{: #ex-20-24-4 }

The program should convert 100 degrees Celsius to Fahrenheit and print 212.0.

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 - 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
```

[Solution 20.24.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-24-4) &middot; [`ex_20_24_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_24_4.py)

### Exercise 20.24.5 — Average of a list of grades
{: #ex-20-24-5 }

This program should print the average of four grades and print 85.0.

```python
def average(grades):
    return sum(grades) / len(grades) - 1

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
```

[Solution 20.24.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-24-5) &middot; [`ex_20_24_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_24_5.py)

## Exercises 20.25.1–20.25.5

### Exercise 20.25.1 — Copying a seating chart
{: #ex-20-25-1 }

This program should copy a seating chart so editing the copy leaves the original unchanged.

```python
import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = original.copy()
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
```

[Solution 20.25.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-25-1) &middot; [`ex_20_25_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_25_1.py)

### Exercise 20.25.2 — Backing up monthly budgets
{: #ex-20-25-2 }

The program should make an independent copy of a nested budget so changes do not leak back.

```python
import copy

budgets = [[100, 200], [300, 400]]
saved = budgets[:]
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
```

[Solution 20.25.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-25-2) &middot; [`ex_20_25_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_25_2.py)

### Exercise 20.25.3 — Duplicating a tic-tac-toe board
{: #ex-20-25-3 }

This program should duplicate a game board so the duplicate can be edited safely.

```python
import copy

board = [["X", "O"], ["O", "X"]]
trial = list(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
```

[Solution 20.25.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-25-3) &middot; [`ex_20_25_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_25_3.py)

### Exercise 20.25.4 — Snapshotting weekly readings
{: #ex-20-25-4 }

The program should take a snapshot of nested sensor readings that stays fixed.

```python
import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = readings.copy()
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
```

[Solution 20.25.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-25-4) &middot; [`ex_20_25_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_25_4.py)

### Exercise 20.25.5 — Cloning a recipe with sub-steps
{: #ex-20-25-5 }

This program should clone a recipe (with nested steps) so editing the clone is safe.

```python
import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = recipe[:]
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
```

[Solution 20.25.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-25-5) &middot; [`ex_20_25_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_25_5.py)

## Exercises 20.26.1–20.26.5

### Exercise 20.26.1 — Collecting quiz answers
{: #ex-20-26-1 }

Each call should start with an empty answer sheet and add one answer.

```python
def record_answer(answer, sheet=[]):
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
```

[Solution 20.26.1]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-26-1) &middot; [`ex_20_26_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_26_1.py)

### Exercise 20.26.2 — Building a grocery list
{: #ex-20-26-2 }

Each call should begin with a fresh, empty cart and add one item.

```python
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
```

[Solution 20.26.2]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-26-2) &middot; [`ex_20_26_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_26_2.py)

### Exercise 20.26.3 — Logging a single temperature
{: #ex-20-26-3 }

Each call should return a new log holding only the reading passed in.

```python
def log_reading(reading, log=[]):
    log.append(reading)
    return log

print(log_reading(21.5))  # expected [21.5]
print(log_reading(19.0))  # expected [19.0]
```

[Solution 20.26.3]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-26-3) &middot; [`ex_20_26_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_26_3.py)

### Exercise 20.26.4 — Tracking a player's scores
{: #ex-20-26-4 }

Each call should start a brand-new scoreboard with just the given score.

```python
def new_scoreboard(score, board=[]):
    board.append(score)
    return board

print(new_scoreboard(10))  # expected [10]
print(new_scoreboard(20))  # expected [20]
```

[Solution 20.26.4]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-26-4) &middot; [`ex_20_26_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_26_4.py)

### Exercise 20.26.5 — Noting one ingredient
{: #ex-20-26-5 }

Each call should produce a fresh list containing only the ingredient given.

```python
def note_ingredient(name, items=[]):
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
```

[Solution 20.26.5]({{ site.baseurl }}/ep/solutions/20-common-pitfalls/#sol-20-26-5) &middot; [`ex_20_26_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_20_26_5.py)

