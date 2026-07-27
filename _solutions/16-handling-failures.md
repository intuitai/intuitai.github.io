---
title: "Chapter 16: Handling Failures — Solutions"
short_title: "Ch. 16 — Handling Failures"
layout: post
permalink: /ep/solutions/16-handling-failures/
order: 9
chapter: 16
---

Worked solutions to the 20 *Find the Bug* exercises in [Chapter 16: Handling Failures]({{ site.baseurl }}/ep/exercises/16-handling-failures/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 16.1.1–16.1.5

### Solution 16.1.1 — Reading an age
{: #sol-16-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The `int(raw)` call happens *outside* the `try`, so a non-numeric entry raises `ValueError` before the `except` can catch it and the program crashes. Move the conversion inside the `try` so the failing line is actually protected.

```python
while True:
    raw = input("Enter your age in years: ")
    try:
        age = int(raw)
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
```

[Back to Exercise 16.1.1]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-1-1) &middot; [`sol_16_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_1_1.py)

</details>

### Solution 16.1.2 — Parsing a price
{: #sol-16-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The exception name is misspelled `VlaueError`, which Python treats as an unknown name; when `float` raises the real `ValueError` it is not caught and the program crashes (and the wrong name itself raises `NameError`). Spell it `ValueError`.

```python
try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except ValueError:
    print("That was not a valid price.")
```

[Back to Exercise 16.1.2]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-1-2) &middot; [`sol_16_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_1_2.py)

</details>

### Solution 16.1.3 — Counting jellybeans
{: #sol-16-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

There is no `break` after a successful read, so even on valid input the `while True` loop never ends — it keeps re-asking forever. Add `break` once a valid count is printed.

```python
while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
        break
    except ValueError:
        print("Please type a whole number.")
```

[Back to Exercise 16.1.3]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-1-3) &middot; [`sol_16_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_1_3.py)

</details>

### Solution 16.1.4 — Temperature reading
{: #sol-16-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `except ValueError` line is missing its colon, so the file will not parse. Add the colon.

```python
try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError:
    print("That was not a valid number.")
```

[Back to Exercise 16.1.4]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-1-4) &middot; [`sol_16_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_1_4.py)

</details>

### Solution 16.1.5 — Validating a test score
{: #sol-16-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `except` block silently keeps the invalid text by assigning `score = raw`, so the program reports nonsense as a score instead of rejecting it. Validation should re-prompt or refuse bad input rather than swallow it.

```python
while True:
    raw = input("Enter your test score: ")
    try:
        score = int(raw)
        break
    except ValueError:
        print("Please type a whole number.")
print("Your score is", score)
```

[Back to Exercise 16.1.5]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-1-5) &middot; [`sol_16_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_1_5.py)

</details>

## Solutions 16.2.1–16.2.5

### Solution 16.2.1 — Splitting a bill
{: #sol-16-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Dividing by zero raises `ZeroDivisionError`, but the code catches `ValueError`, so the real error escapes and the program crashes. Catch `ZeroDivisionError`.

```python
bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ZeroDivisionError:
    print("There must be at least one person.")
```

[Back to Exercise 16.2.1]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-2-1) &middot; [`sol_16_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_2_1.py)

</details>

### Solution 16.2.2 — Adding a measurement
{: #sol-16-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Adding an integer to a string raises `TypeError`, but the code catches `ZeroDivisionError`, so the error is not caught and the program crashes. Catch `TypeError`.

```python
total = 100
new_value = "twelve"
try:
    total = total + new_value
except TypeError:
    print("That measurement was not a number.")
print("Total is", total)
```

[Back to Exercise 16.2.2]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-2-2) &middot; [`sol_16_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_2_2.py)

</details>

### Solution 16.2.3 — Average speed
{: #sol-16-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The broad `except Exception` is listed first, and because `ZeroDivisionError` is a subclass of `Exception`, the first handler swallows a zero-time error and prints the misleading “Distance was not a number” message; the specific `ZeroDivisionError` handler is unreachable. Put the specific handler before the general one.

```python
distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except ZeroDivisionError:
    print("Time cannot be zero.")
except Exception:
    print("Distance was not a number.")
```

[Back to Exercise 16.2.3]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-2-3) &middot; [`sol_16_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_2_3.py)

</details>

### Solution 16.2.4 — Looking up a grade
{: #sol-16-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Looking up a missing dictionary key raises `KeyError`, but the code catches `ValueError`, so the lookup failure is not handled and the program crashes. Catch `KeyError`.

```python
grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except KeyError:
    print("No grade recorded for", name)
```

[Back to Exercise 16.2.4]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-2-4) &middot; [`sol_16_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_2_4.py)

</details>

### Solution 16.2.5 — Percent off
{: #sol-16-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The broad `except Exception` comes first, and since `ZeroDivisionError` is a subclass of `Exception`, a zero divisor is caught by the first handler and reported as “not a valid number”; the specific `ZeroDivisionError` handler can never run. List the specific handler before the general one.

```python
price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except ZeroDivisionError:
    print("The divisor cannot be zero.")
except Exception:
    print("That was not a valid number.")
```

[Back to Exercise 16.2.5]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-2-5) &middot; [`sol_16_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_2_5.py)

</details>

## Solutions 16.3.1–16.3.5

### Solution 16.3.1 — Confirming a conversion
{: #sol-16-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The success line is printed twice — once inside `try` and again in `else`. Code that should run only on success belongs in `else`, not in `try`; remove the duplicate from the `try` block.

```python
text = "42"
try:
    number = int(text)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
```

[Back to Exercise 16.3.1]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-3-1) &middot; [`sol_16_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_3_1.py)

</details>

### Solution 16.3.2 — Area of a rectangle
{: #sol-16-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `else` block computes `area` but never prints it, so the program produces no visible result on success. Print the area in the `else` block.

```python
try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
    print("Area:", area)
```

[Back to Exercise 16.3.2]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-3-2) &middot; [`sol_16_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_3_2.py)

</details>

### Solution 16.3.3 — Doubling a recipe
{: #sol-16-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The doubling work that should run only after a successful conversion is placed in the `try` block; if `cups * 2` or the print logic ever failed it would be wrongly treated as an input error. The success-only computation belongs in `else`, leaving only the risky conversion in `try`.

```python
try:
    cups = float(input("How many cups? "))
except ValueError:
    print("That was not a number.")
else:
    doubled = cups * 2
    print("You need", doubled, "cups.")
```

[Back to Exercise 16.3.3]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-3-3) &middot; [`sol_16_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_3_3.py)

</details>

### Solution 16.3.4 — Safe square root
{: #sol-16-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `try` keyword is missing its colon, so the file will not parse. Add the colon after `try`.

```python
import math

try:
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
```

[Back to Exercise 16.3.4]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-3-4) &middot; [`sol_16_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_3_4.py)

</details>

### Solution 16.3.5 — Tax on a purchase
{: #sol-16-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The tax formula uses addition (`amount + 0.08`) instead of multiplication, so it adds eight cents rather than computing 8 percent of the amount. Use `amount * 0.08`.

```python
try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount * 0.08
    print("Tax is", tax)
```

[Back to Exercise 16.3.5]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-3-5) &middot; [`sol_16_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_3_5.py)

</details>

## Solutions 16.4.1–16.4.5

### Solution 16.4.1 — Closing a report
{: #sol-16-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The closing line sits inside the `except` block, so it prints only when the division fails; on the normal path it never runs. Move the always-run line into a `finally` block.

```python
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done with the calculation.")
```

[Back to Exercise 16.4.1]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-4-1) &middot; [`sol_16_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_4_1.py)

</details>

### Solution 16.4.2 — Releasing the scale
{: #sol-16-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

“Scale released” must always print, but it is in the `else` block, which runs only when no exception occurs; on bad input it is skipped. Use `finally` so it runs whether or not an error happened.

```python
try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
finally:
    print("Scale released.")
```

[Back to Exercise 16.4.2]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-4-2) &middot; [`sol_16_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_4_2.py)

</details>

### Solution 16.4.3 — Logging an attempt
{: #sol-16-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `finally` keyword is missing its colon, so the file will not parse. Add the colon after `finally`.

```python
try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally:
    print("Attempt logged.")
```

[Back to Exercise 16.4.3]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-4-3) &middot; [`sol_16_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_4_3.py)

</details>

### Solution 16.4.4 — Final tally
{: #sol-16-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The tally line sits inside the `try` right after the division, so a `ZeroDivisionError` skips it. A line that must always run belongs in a `finally` block, which executes whether or not an exception occurs.

```python
points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
except ZeroDivisionError:
    print("No rounds played.")
finally:
    print("Final tally complete.")
```

[Back to Exercise 16.4.4]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-4-4) &middot; [`sol_16_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_4_4.py)

</details>

### Solution 16.4.5 — Cleanup message
{: #sol-16-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The clauses are out of order: `finally` appears before `except`, which is not allowed — `except` (and `else`) must come before `finally`. Reorder so `except` precedes `finally`.

```python
try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
except ValueError:
    print("That was not a number.")
finally:
    print("Sensor reset.")
```

[Back to Exercise 16.4.5]({{ site.baseurl }}/ep/exercises/16-handling-failures/#ex-16-4-5) &middot; [`sol_16_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_16_4_5.py)

</details>

