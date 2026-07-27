---
title: About the Book
seo_title: "About Everyday Programming — Who the Book Is For"
description: >
  Who Everyday Programming is written for, what it assumes you already know
  (tenth-grade arithmetic and nothing else), how its seven parts fit together,
  and why it explains the parts other beginner programming books skip.
layout: post
permalink: /ep/book/about/
order: 1
---

*Everyday Programming, Volume I: Basics of Computer Programs* is a first course
in programming for people who have never written a line of code, and who are
not sure they are the kind of person who can.

They are. That is the premise of the book.

## The idea

Programming is the act of describing a solution precisely enough that a machine
can carry it out. Both halves of that sentence need teaching, and most
introductory books only teach the second one.

So the book is built in the order the skill is actually acquired:

1. **A vocabulary for describing things exactly.** Logic, sets, remainders,
   variables, functions, sequences, counting, graphs, binary numbers, hashing,
   recursion. Nothing beyond a tenth-grade classroom, and every idea introduced
   because a later chapter needs it — never for its own sake.
2. **A habit of taking problems apart.** Pseudocode first, on paper, then the
   translation into Python. Chapter 2 walks the whole path once, slowly, before
   any syntax has to be memorized.
3. **The language itself.** Data structures, objects, operators, input and
   output, control flow, functions, scope, modules, packages.
4. **The part nobody teaches beginners.** Quality, failure handling, testing
   with pytest, debugging, tooling, and the specific mistakes that trip people
   up over and over.

Chapter 1 contains no code at all, and Chapter 2 does not reach Python until
the problem in front of it has already been solved on paper. That ordering is
deliberate, and it is the single biggest difference between this book and the
one next to it on the shelf.

## Find the Bug

The book's other distinguishing feature is an exercise bank of unusual size and
unusual shape: **445 programs, each containing exactly one mistake.**

They are not "write a function that…" problems. They are short, complete,
realistic programs — a quiz total, a bill split four ways, a list of planets, a
temperature conversion — that are *almost* right. Your job is to read carefully
and find the one thing that is wrong.

This trains the skill that separates programmers from tutorial-finishers.
Writing code you have just been shown is easy. Reading code and locating the
defect is the actual job, and it is almost never taught directly.

Every solution names the bug as one of three kinds:

- **Syntax** — Python cannot even parse it. A missing colon, an unclosed
  parenthesis. The program never runs.
- **Runtime** — it parses and starts, then fails partway. Adding a string to an
  integer, indexing past the end of a list.
- **Logical** — it parses, runs, finishes without complaint, and gives the wrong
  answer. The most dangerous kind, and the one beginners are never warned about.

Sorting a failure into one of those three bins is the first move of any real
debugging session, and after four hundred repetitions it becomes automatic.

The exercises are distributed through twelve chapters, so each one lands
directly after the material it tests. The worked solutions are collected in
Chapter 21, and cross-referenced both ways.

## How it is put together

The book is typeset in the style of the LaTeX edition of *Structure and
Interpretation of Computer Programs* — Linux Libertine text, violet chapter
drop capitals, and syntax-colored Python listings — because a book you have to
sit with for four hundred pages should be pleasant to sit with.

Illustrations are used where a picture genuinely helps: a wall clock for modular
arithmetic, a sunflower head for the Fibonacci sequence, a seating chart for
nested lists, Escher's drawing hands for recursion.

## The practical details

| | |
|---|---|
| **Title** | Everyday Programming, Volume I: Basics of Computer Programs |
| **Author** | Dr. Nobel Khandaker |
| **Edition** | First Edition |
| **Publisher** | Intramotev Press |
| **Length** | 21 chapters in 7 parts, 400+ pages |
| **Exercises** | 445, with 445 worked solutions |
| **Language** | Python 3 — standard library throughout; `pytest` for the testing chapter |
| **License** | Apache License 2.0 |

## Read some of it first

Part I — Chapters 1 and 2, the whole of the mathematical grounding and the
problem-solving method — is [available free as a PDF]({{ site.baseurl }}/ep/book/sample/),
typeset exactly as the printed book is. Twenty-six pages, no watermark, nothing
withheld.

If Part I works for you, the rest of the book will.
