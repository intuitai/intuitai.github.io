---
title: "Chapter 16: Handling Failures"
short_title: "Ch. 16 — Handling Failures"
layout: post
permalink: /ep/exercises/16-handling-failures/
order: 9
chapter: 16
exercise_count: 20
---

20 *Find the Bug* exercises from Chapter 16 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 16 solutions]({{ site.baseurl }}/ep/solutions/16-handling-failures/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 16.1.1–16.1.5

### Exercise 16.1.1 — Reading an age
{: #ex-16-1-1 }

This program should keep asking until the user types a whole number for their age, then print it.

```python
while True:
    raw = input("Enter your age in years: ")
    age = int(raw)
    try:
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
```

[Solution 16.1.1]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-1-1) &middot; [`ex_16_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_1_1.py)

### Exercise 16.1.2 — Parsing a price
{: #ex-16-1-2 }

This program should read a price like `"4.99"` and print double it, recovering from bad input.

```python
try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except VlaueError:
    print("That was not a valid price.")
```

[Solution 16.1.2]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-1-2) &middot; [`ex_16_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_1_2.py)

### Exercise 16.1.3 — Counting jellybeans
{: #ex-16-1-3 }

This program reads how many jellybeans are in a jar and prints the count, retrying on bad input.

```python
while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
    except ValueError:
        print("Please type a whole number.")
```

[Solution 16.1.3]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-1-3) &middot; [`ex_16_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_1_3.py)

### Exercise 16.1.4 — Temperature reading
{: #ex-16-1-4 }

This program reads a Celsius temperature and converts it to Fahrenheit, handling bad input.

```python
try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError
    print("That was not a valid number.")
```

[Solution 16.1.4]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-1-4) &middot; [`ex_16_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_1_4.py)

### Exercise 16.1.5 — Validating a test score
{: #ex-16-1-5 }

This program should accept a score the user types only if it is a whole number, then print it.

```python
raw = input("Enter your test score: ")
try:
    score = int(raw)
except ValueError:
    score = raw
print("Your score is", score)
```

[Solution 16.1.5]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-1-5) &middot; [`ex_16_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_1_5.py)

## Exercises 16.2.1–16.2.5

### Exercise 16.2.1 — Splitting a bill
{: #ex-16-2-1 }

This program divides a restaurant bill among friends and should report when there are zero friends.

```python
bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ValueError:
    print("There must be at least one person.")
```

[Solution 16.2.1]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-2-1) &middot; [`ex_16_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_2_1.py)

### Exercise 16.2.2 — Adding a measurement
{: #ex-16-2-2 }

This program adds a typed measurement to a running total and warns if the text is not a number.

```python
total = 100
new_value = "twelve"
try:
    total = total + new_value
except ZeroDivisionError:
    print("That measurement was not a number.")
print("Total is", total)
```

[Solution 16.2.2]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-2-2) &middot; [`ex_16_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_2_2.py)

### Exercise 16.2.3 — Average speed
{: #ex-16-2-3 }

This program reads a distance and a time, divides to get average speed, and should report a typed-in non-number and a zero time with separate messages.

```python
distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except Exception:
    print("Distance was not a number.")
except ZeroDivisionError:
    print("Time cannot be zero.")
```

[Solution 16.2.3]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-2-3) &middot; [`ex_16_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_2_3.py)

### Exercise 16.2.4 — Looking up a grade
{: #ex-16-2-4 }

This program looks up a student's grade in a dictionary and reports a clear message if the name is missing.

```python
grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except ValueError:
    print("No grade recorded for", name)
```

[Solution 16.2.4]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-2-4) &middot; [`ex_16_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_2_4.py)

### Exercise 16.2.5 — Percent off
{: #ex-16-2-5 }

This program reads a typed divisor, builds a fraction from it, and should report a non-number and a zero divisor with separate messages.

```python
price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except Exception:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("The divisor cannot be zero.")
```

[Solution 16.2.5]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-2-5) &middot; [`ex_16_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_2_5.py)

## Exercises 16.3.1–16.3.5

### Exercise 16.3.1 — Confirming a conversion
{: #ex-16-3-1 }

This program converts a string to a number and, only when that succeeds, prints a success line.

```python
text = "42"
try:
    number = int(text)
    print("Conversion worked:", number)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
```

[Solution 16.3.1]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-3-1) &middot; [`ex_16_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_3_1.py)

### Exercise 16.3.2 — Area of a rectangle
{: #ex-16-3-2 }

This program reads two side lengths and, if both parse, prints the area in the `else` block.

```python
try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
```

[Solution 16.3.2]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-3-2) &middot; [`ex_16_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_3_2.py)

### Exercise 16.3.3 — Doubling a recipe
{: #ex-16-3-3 }

This program reads a cup amount and, when valid, prints the doubled amount using `else`.

```python
try:
    cups = float(input("How many cups? "))
    doubled = cups * 2
    print("You need", doubled, "cups.")
except ValueError:
    print("That was not a number.")
else:
    print("Measurement accepted.")
```

[Solution 16.3.3]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-3-3) &middot; [`ex_16_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_3_3.py)

### Exercise 16.3.4 — Safe square root
{: #ex-16-3-4 }

This program reads a number and, only if it parses, prints its square root in the `else` block.

```python
import math

try
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
```

[Solution 16.3.4]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-3-4) &middot; [`ex_16_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_3_4.py)

### Exercise 16.3.5 — Tax on a purchase
{: #ex-16-3-5 }

This program parses a purchase amount and, when it succeeds, computes 8 percent tax in the `else` block.

```python
try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount + 0.08
    print("Tax is", tax)
```

[Solution 16.3.5]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-3-5) &middot; [`ex_16_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_3_5.py)

## Exercises 16.4.1–16.4.5

### Exercise 16.4.1 — Closing a report
{: #ex-16-4-1 }

This program divides two numbers and should always print a closing line, whether or not the division fails.

```python
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
    print("Done with the calculation.")
```

[Solution 16.4.1]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-4-1) &middot; [`ex_16_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_4_1.py)

### Exercise 16.4.2 — Releasing the scale
{: #ex-16-4-2 }

This program weighs an item and must always print that the scale is released, even when input is bad.

```python
try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
else:
    print("Scale released.")
```

[Solution 16.4.2]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-4-2) &middot; [`ex_16_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_4_2.py)

### Exercise 16.4.3 — Logging an attempt
{: #ex-16-4-3 }

This program parses a count and must always log that an attempt was made, regardless of success.

```python
try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally
    print("Attempt logged.")
```

[Solution 16.4.3]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-4-3) &middot; [`ex_16_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_4_3.py)

### Exercise 16.4.4 — Final tally
{: #ex-16-4-4 }

Whatever happens above, this program must always print `Final tally complete.` at the end. With `rounds` set to 0 it currently does not.

```python
points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
    print("Final tally complete.")
except ZeroDivisionError:
    print("No rounds played.")
```

[Solution 16.4.4]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-4-4) &middot; [`ex_16_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_4_4.py)

### Exercise 16.4.5 — Cleanup message
{: #ex-16-4-5 }

This program reads a distance and must always print a cleanup line at the very end, no matter what happens.

```python
try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
finally:
    print("Sensor reset.")
except ValueError:
    print("That was not a number.")
```

[Solution 16.4.5]({{ site.baseurl }}/ep/solutions/16-handling-failures/#sol-16-4-5) &middot; [`ex_16_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_16_4_5.py)

