---
title: Everyday Programming
seo_title: "Everyday Programming — A Free Python Book for Absolute Beginners"
description: >
  A first course in Python for absolute beginners, built on nothing more than
  tenth-grade mathematics. Twenty-one chapters in seven parts, 445 free Find the
  Bug exercises with full worked solutions, and Chapters 1 and 2 free to download.
layout: post
permalink: /ep/
order: 0
# Disables excerpt extraction. Jekyll takes the excerpt as everything up to the
# first blank line, and the Liquid comment below spans several -- which makes it
# warn about a "modified excerpt" on every build. Nothing on this site renders
# excerpts, so the fix is to not generate one.
excerpt_separator: ""
---

{%- comment -%}
layout: post, not home.

The theme's home layout emits a rel="next" link built from site.baseurl and the
first post's URL, guarded by a truthiness test on the reversed post list. An
empty array is truthy in Liquid, so with no _posts the guard passes anyway; on a
site with a baseurl the href still came out non-empty by accident, but this site
is served from an apex domain with an empty baseurl, so the href is empty and
html-proofer rejects it.

The post layout also gives this page working prev/next arrows through the book
collection, which the home layout does not.

Note this is a Liquid comment rather than an HTML one: Liquid tokenises tags
inside HTML comments too, so spelling the guard out literally here would be a
syntax error rather than documentation.
{%- endcomment -%}

<div class="ep-hero" markdown="0">
  <div class="ep-hero__cover">
    <img src="{{ site.baseurl }}/ep/assets/img/cover.png"
         alt="Cover of Everyday Programming, Volume I: Basics of Computer Programs, by Dr. Nobel Khandaker">
  </div>
  <div class="ep-hero__body">
    <span class="ep-kicker">Volume I &middot; Basics of Computer Programs</span>
    <p class="ep-tagline"><strong>You do not need to be a &ldquo;math person&rdquo; to program.</strong>
    You need tenth-grade arithmetic, a habit of thinking a problem through, and
    someone willing to explain the parts everybody else skips. This book is that
    explanation.</p>
    <p>A first course in Python for people starting from zero &mdash; written by a
    lead engineer with a doctorate in computer science and twelve years shipping
    software, for the reader who has opened three tutorials and quietly closed
    all three.</p>
    <div class="ep-actions">
      <a class="ep-btn ep-btn--primary" href="{{ site.baseurl }}/ep/assets/pdf/everyday-programming-sample-chapters-1-2.pdf" download="everyday-programming-chapters-1-2.pdf">Download chapters 1&ndash;2 free (PDF)</a>
      <a class="ep-btn ep-btn--ghost" href="{{ site.baseurl }}/ep/book/exercises/">Try the 445 exercises</a>
    </div>
  </div>
</div>

<ul class="ep-facts" markdown="0">
  <li><b>21</b><span>chapters, in seven parts</span></li>
  <li><b>445</b><span>Find the Bug exercises</span></li>
  <li><b>445</b><span>full worked solutions</span></li>
  <li><b>400+</b><span>pages, start to finish</span></li>
</ul>

## Why most first programming books do not work

They start at line one of a program. `print("Hello, world")`, then variables,
then loops — and somewhere around the third chapter the reader realizes they
are copying symbols without knowing what any of it *means*. The book never said
what a variable actually is, because the book assumed you already knew.

*Everyday Programming* starts two chapters earlier than that.

Part I barely touches a keyboard. It builds the small vocabulary that
programming quietly assumes — logic, sets, remainders, variables, functions,
sequences, counting, graphs, binary numbers — and it does so at the level of a
tenth-grade classroom, with a wall clock for modular arithmetic and a seashell
for the Fibonacci sequence. Chapter 1 contains no code at all. Chapter 2 then
teaches you to take a problem apart on paper, in plain pseudocode, and only
translates it into Python once the thinking is already done.

So by the time you meet your first real Python program, you already know what
every line of it is for.

## Learn to read code, not just type it

Here is the part that makes this book different from the shelf next to it.

Anyone can follow along while a book types a working program. That is not the
skill. The skill — the one that separates people who can program from people
who have finished a tutorial — is looking at code that is *nearly* right and
seeing exactly where it goes wrong.

So the book contains **445 Find the Bug exercises**. Each is a short, realistic
program: a quiz score, a shopping list, a temperature conversion. Most run
three to ten lines, and none runs to more than twenty-two. And each one hides
**exactly one** mistake.

<div class="ep-note" markdown="1">
**Exercise 5.1.1 — Total points.** A quiz has 3 sections worth 20, 30, and 25 points.
The program should print the total, 75.

```python
section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 - section3
print(total)   # 75
```

Found it? The [worked solution]({{ site.baseurl }}/ep/solutions/05-data-structures/#sol-5-1-1)
names the bug as **logical** — the program is valid Python and runs happily; it
just answers the wrong question. That distinction is the whole lesson.
</div>

Every solution names the bug as **syntax**, **runtime**, or **logical**,
explains *why* the original misbehaved, and shows the corrected program. Learn
to sort mistakes into those three bins and debugging stops being luck.

All 890 programs are [on this site]({{ site.baseurl }}/ep/book/exercises/), as web
pages and as `.py` files you can download and run.

## Who this book is for

- **Absolute beginners.** No prior programming. No calculus. If you can work out
  how much change you are owed, you have enough mathematics to start.
- **Self-taught learners who stalled.** If you have done a video course and
  still cannot write a program from a blank file, the missing piece is usually
  Part I and the debugging habit — both are here.
- **Career changers.** A structured path from first principles to writing,
  testing, and debugging real Python, without assuming a computer-science degree
  you do not have.
- **Students and teachers.** Seven parts you can map onto a term, and an
  exercise bank of 445 problems with worked solutions, free to use under
  Apache 2.0.

<div class="ep-note" markdown="1">
**Who it is *not* for.** If you already write Python comfortably and want
advanced material — async, type systems, performance work — this is the wrong
volume. It is called *Basics of Computer Programs* on purpose.
</div>

## What you will be able to do by the end

Read a Python program and say what it does. Write one from a blank file. Choose
the right data structure and explain why. Break a problem into functions.
Organize code into modules and packages. Write tests with pytest. Handle
failures instead of crashing. And when something breaks — because it will —
work out where, methodically, instead of changing lines at random.

The last two parts are about exactly that: quality, testing, debugging, the
tools of the trade, and a catalog of the 26 mistakes that catch beginners
most often, each one named and defused.

## Start here

- **[Read chapters 1 and 2 free]({{ site.baseurl }}/ep/book/sample/)** — the whole of
  Part I, 26 pages, typeset exactly as the book is.
- **[Browse the table of contents]({{ site.baseurl }}/ep/book/table-of-contents/)** —
  all 21 chapters and 130 sections.
- **[Work the exercises]({{ site.baseurl }}/ep/book/exercises/)** — 445 bugs waiting
  to be found, with solutions when you want them.
- **[About the author]({{ site.baseurl }}/ep/book/author/)**

<p style="margin-top:2.5em;color:#57606a;font-size:0.92em;">
<em>Everyday Programming</em>, Volume I: Basics of Computer Programs &mdash;
First Edition, published by Intramotev Press. Text and code licensed under the
Apache License 2.0.
</p>
