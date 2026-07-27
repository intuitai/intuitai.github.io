---
title: Exercises and Solutions
layout: post
permalink: /ep/book/exercises/
order: 4
---

Every *Find the Bug* exercise in the book, free, with every worked solution —
{% assign total = 0 %}{% for ex in site.exercises %}{% assign total = total | plus: ex.exercise_count %}{% endfor %}**{{ total }}** of them, across
{{ site.exercises | size }} chapters. Read them here, or download all
{{ total | times: 2 }} programs as `.py` files and run them.

<div class="ep-actions" markdown="0">
  <a class="ep-btn ep-btn--primary" href="{{ site.baseurl }}/ep/assets/code/everyday-programming-exercises.zip">Download all {{ site.data.downloads.program_count }} programs (.zip, {{ site.data.downloads.exercise_zip_size }})</a>
  <a class="ep-btn ep-btn--ghost" href="{{ site.baseurl }}/ep/exercises/05-data-structures/">Start with Chapter 5</a>
</div>

## How to use them

Each exercise is a short, complete program that does something recognizable —
totalling a quiz, splitting a bill, listing planets — and hides **exactly one**
mistake. Nothing else about it is wrong.

The productive order is:

1. **Read it and predict.** Say out loud what you expect the program to print.
   The comment on the last line usually tells you what it *should* print.
2. **Find the difference.** If your prediction and the intended output disagree,
   the gap is the bug.
3. **Run it.** Confirm you were right — or find out you were not, which is more
   useful.
4. **Then open the solution.** Not before. The diagnosis is where the learning
   is, and reading it first spends the exercise for nothing.

Solutions stay folded behind a click for exactly that reason.

## The three kinds of bug

Every solution names which kind it is. Learning to sort a failure into one of
these three bins, quickly, is the first move of any real debugging session.

| Kind | What happens | Example | Here |
|---|---|---|---|
| **Syntax** | Python cannot parse the file. Nothing runs at all. | A missing `:` after `if` | {{ site.data.downloads.bug_kinds.syntax }} |
| **Runtime** | It starts, then fails partway with an exception. | `count + "10"` — you cannot add an `int` and a `str` | {{ site.data.downloads.bug_kinds.runtime }} |
| **Logical** | It runs, finishes cleanly, and is wrong. | `students / teams` where `students // teams` was meant | {{ site.data.downloads.bug_kinds.logical }} |

The third kind is the one beginners are never warned about, and the one that
causes real damage — which is why it is deliberately the largest group here:
{{ site.data.downloads.bug_kinds.logical }} of the
{{ site.data.downloads.exercise_count }} exercises are logical bugs, more than
syntax and runtime combined.

{% assign counted = site.data.downloads.bug_kinds.syntax | plus: site.data.downloads.bug_kinds.runtime | plus: site.data.downloads.bug_kinds.logical %}
{%- assign both = site.data.downloads.exercise_count | minus: counted %}
{%- if both > 0 %}
<p style="font-size:0.88em;color:#57606a;">The three counts come to
{{ counted }}; the remaining {% if both == 1 %}exercise sits{% else %}{{ both }} exercises sit{% endif %}
on the line between runtime and logical, and {% if both == 1 %}its solution names{% else %}their solutions name{% endif %} both.</p>
{%- endif %}

## By chapter

<table class="ep-chapters">
  <thead>
    <tr><th>Chapter</th><th>Exercises</th><th>Solutions</th><th>Count</th></tr>
  </thead>
  <tbody>
  {%- for ex in site.exercises %}
    {%- assign sol = nil -%}
    {%- for s in site.solutions -%}
      {%- if s.chapter == ex.chapter -%}{%- assign sol = s -%}{%- endif -%}
    {%- endfor -%}
    <tr>
      <td>{{ ex.short_title }}</td>
      <td><a href="{{ site.baseurl }}{{ ex.url }}">Exercises</a></td>
      <td>{%- if sol %}<a href="{{ site.baseurl }}{{ sol.url }}">Solutions</a>{% else %}&mdash;{% endif -%}</td>
      <td>{{ ex.exercise_count }}</td>
    </tr>
  {%- endfor %}
  </tbody>
</table>

## Running them on your own machine

The archive unpacks into two folders:

```text
everyday-programming-exercises/
    exercises/ex_<chapter>_<group>_<n>.py    the program with the bug in it
    solutions/sol_<chapter>_<group>_<n>.py   the diagnosis and the fix
```

Almost every program runs on a stock Python 3 with nothing installed — the
imports are all standard library (`math`, `copy`, `random`, `statistics`). Two
sets need a little more:

- **Chapter 17** (testing) uses `pytest`: `pip install pytest`.
- **Section 13.2** (writing your own module) imports modules such as
  `conversions` and `shapes` that *you* are meant to have written. Those four
  exercises are about the import mechanism itself, so they raise
  `ModuleNotFoundError` until you create the module beside them — the chapter
  walks you through it.

Everything else just runs:

```console
$ python3 exercises/ex_5_1_1.py
25
```

That `25` is the bug: the program was supposed to print `75`.

Some exercises will not run at all, and that is the point — a `SyntaxError` or a
traceback *is* the bug you were asked to find. Each file opens with a docstring
saying what the program was supposed to do, so you always know what correct
looks like.

<div class="ep-note" markdown="1">
**For teachers.** All 445 exercises and solutions are licensed under Apache 2.0,
the same as the book. Use them in a class, a workshop, or a problem set. The
per-chapter pages are stable URLs you can link to directly, and the numbering
matches the printed book, so `Exercise 9.4.2` means the same thing on paper and
on screen.
</div>

## A worked example

<div class="ep-note" markdown="1">
**Exercise 5.2.1 — Average temperature.** Three readings are 20.0, 22.0 and 24.0.
The program should print their average, 22.0.

```python
reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = reading1 + reading2 + reading3 / 3
print(average)   # 22.0
```

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Without parentheses, only `reading3 / 3` is divided — operator precedence puts
division ahead of addition — so the program prints `50.0`. Wrap the addition in
parentheses before dividing.

```python
average = (reading1 + reading2 + reading3) / 3
print(average)   # 22.0
```

</details>
</div>

That is the shape of all 445 of them. [Start with Chapter 5]({{ site.baseurl }}/ep/exercises/05-data-structures/).
