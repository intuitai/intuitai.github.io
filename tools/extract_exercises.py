#!/usr/bin/env python3
"""Generate the site's exercise and solution pages from the book's LaTeX sources.

The 445 "Find the Bug" exercises live in twelve chapter files of the
everyday-programming manuscript; the 445 matching worked solutions are
collected in python_snippets_solutions.tex. This script is the only thing that
writes _exercises/, _solutions/ and assets/code -- edit the manuscript and
re-run, never hand-edit the generated pages.

    ./tools/extract_exercises.py --manuscript ../manuscripts/everyday-programming

The manuscript is uniform to a degree that makes a strict parser the right
choice: every one of the 890 \\paragraph blocks contains exactly one
\\begin{minted}{python} listing, and every exercise number has exactly one
solution. All four of those invariants are asserted rather than worked around,
so a change to the book's conventions fails here loudly instead of quietly
producing half-parsed pages.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

# Chapter titles are keyed by the leading component of the exercise number, not
# by source filename. The two do not agree: python_list.tex holds the 6.x
# exercises because it is a \section continuing the Objects chapter, and
# python_quality.tex holds the 16.x set because it declares two chapters.
# Numbers and titles both come from everyday-programming.toc.
CHAPTERS: dict[int, tuple[str, str]] = {
    5: ("Data Structures", "05-data-structures"),
    6: ("Objects", "06-objects"),
    7: ("Operators", "07-operators"),
    8: ("Input and Output", "08-input-and-output"),
    9: ("Control Flow", "09-control-flow"),
    10: ("Functions", "10-functions"),
    11: ("Scoping", "11-scoping"),
    13: ("Modules", "13-modules"),
    16: ("Handling Failures", "16-handling-failures"),
    17: ("Testing", "17-testing"),
    18: ("Bugs", "18-bugs"),
    20: ("Common Pitfalls", "20-common-pitfalls"),
}

# Chapter files to scan. The exercises always sit under a \section{Find the Bug
# Exercises}; text above that heading is chapter prose and is skipped.
CHAPTER_SOURCES = [
    "python_bugs.tex",
    "python_control_flow.tex",
    "python_data_structures.tex",
    "python_functions.tex",
    "python_io.tex",
    "python_list.tex",
    "python_modules.tex",
    "python_operators.tex",
    "python_pitfalls.tex",
    "python_quality.tex",
    "python_scoping.tex",
    "python_testing.tex",
]

SOLUTIONS_SOURCE = "python_snippets_solutions.tex"

EXPECTED_TOTAL = 445

# Where the book sits under the site root. The book shares intuitai.org with the
# organization's own landing page, so it lives at /ep rather than at /. This is
# baked into permalinks and cross-links at generation time rather than resolved
# through a Liquid variable, because Jekyll does not evaluate Liquid inside
# front matter -- a permalink has to be a literal string. Keeping the links
# literal too means the two can never drift apart. Set with --prefix.
PREFIX = "/ep"

EXERCISE_HEAD = re.compile(r"\\paragraph\{Exercise ((\d+)\.(\d+)\.(\d+)) --- ")
SOLUTION_HEAD = re.compile(r"\\paragraph\{Solution ((\d+)\.(\d+)\.(\d+)) --- ")
MINTED = re.compile(r"\\begin\{minted\}(?:\[[^\]]*\])?\{python\}\n(.*?)\n?\\end\{minted\}", re.S)

# Only Chapter 5 names its exercise groups, via `% Section N: name` comments
# that the solutions file mirrors. Everywhere else the group heading falls back
# to the range of exercise numbers it covers.
SECTION_COMMENT = re.compile(r"^% Section (\d+): (.+?)\s*$", re.M)


# --------------------------------------------------------------------------
# LaTeX -> Markdown for the short prose that accompanies each exercise
# --------------------------------------------------------------------------

def _read_group(text: str, start: int) -> tuple[str, int]:
    """Read a brace-delimited macro argument beginning at `text[start] == '{'`.

    Nesting has to be tracked rather than regex-matched: \\py{} wraps
    \\mintinline, whose argument is verbatim and routinely contains braces of
    its own -- \\py{{'a': 1}} and \\py{def f(**kw)} both appear in the book.
    """
    assert text[start] == "{", f"expected '{{' at {start}"
    depth, i = 0, start
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError(f"unbalanced braces from offset {start}: {text[start:start + 60]!r}")


# Macros whose single argument becomes literal code, and those that become
# emphasis. Anything not listed here is stripped to its argument.
CODE_MACROS = {"py", "pyk", "texttt", "verb"}
STRONG_MACROS = {"textbf"}
EMPH_MACROS = {"emph", "textit", "textsl"}
DROP_MACROS = {"index", "label", "ref", "nameref", "pageref", "vspace", "smallskip", "noindent"}

SIMPLE_REPLACEMENTS = [
    (r"\ldots", "\u2026"),
    (r"\dots", "\u2026"),
    (r"\%", "%"),
    (r"\_", "_"),
    (r"\&", "&"),
    (r"\#", "#"),
    (r"\$", "$"),
    (r"\{", "{"),
    (r"\}", "}"),
    (r"\,", " "),
    (r"\ ", " "),
]

MARKDOWN_HAZARDS = str.maketrans({c: "\\" + c for c in "*_[]<>"})

# Inline math in the exercise prose is arithmetic, not mathematics: a degree
# sign, a times sign, one pi, a couple of squares. Fourteen spans in the whole
# corpus. Rendering them as Unicode costs nothing and avoids pulling MathJax
# onto every page to typeset "4 x 3".
MATH_SYMBOLS = {
    r"\circ": "°", r"\times": "×", r"\div": "÷",
    r"\pi": "π", r"\cdot": "·", r"\ldots": "…",
    r"\dots": "…", r"\le": "≤", r"\leq": "≤",
    r"\ge": "≥", r"\geq": "≥", r"\neq": "≠",
    r"\approx": "≈", r"\pm": "±", r"\left": "", r"\right": "",
}
SUPERSCRIPTS = str.maketrans("0123456789+-n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ")


def latex_to_markdown(src: str) -> str:
    """Convert one exercise's or solution's prose to Markdown.

    Output is assembled as alternating prose and code spans so that Markdown
    metacharacters can be escaped in the prose without touching the code, where
    a backslash would be a literal character rather than an escape.
    """
    out: list[str] = []
    buf: list[str] = []           # prose pending escape
    i = 0

    def flush() -> None:
        if buf:
            text = "".join(buf).translate(MARKDOWN_HAZARDS)
            out.append(text)
            buf.clear()

    while i < len(src):
        ch = src[i]

        # A bare `$` opens math mode. A currency `\$` never reaches here as an
        # opener -- the backslash branch below consumes both characters via
        # SIMPLE_REPLACEMENTS -- but it can still appear later in the string,
        # and the prose is full of prices ("a \$50 item"). So the search for the
        # closing delimiter steps over escaped dollars rather than stopping at
        # the first `$` character it sees.
        if ch == "$":
            close = i + 1
            while close < len(src):
                if src[close] == "$" and src[close - 1] != "\\":
                    break
                close += 1
            if close >= len(src):               # unpaired: treat as literal
                buf.append(ch)
                i += 1
                continue
            buf.append(math_to_text(src[i + 1:close]))
            i = close + 1
            continue

        if ch != "\\":
            buf.append(ch)
            i += 1
            continue

        # \mintinline{python}|code| -- the delimiter is whatever follows the
        # language argument, and the book uses both | and {.
        m = re.match(r"\\mintinline\{\w+\}", src[i:])
        if m:
            j = i + m.end()
            if src[j] == "{":
                code, j = _read_group(src, j)
            else:
                delim = src[j]
                end = src.index(delim, j + 1)
                code, j = src[j + 1:end], end + 1
            flush()
            out.append(_inline_code(code))
            i = j
            continue

        m = re.match(r"\\([a-zA-Z]+)", src[i:])
        if not m:
            for tex, plain in SIMPLE_REPLACEMENTS:
                if src.startswith(tex, i):
                    buf.append(plain)
                    i += len(tex)
                    break
            else:
                buf.append(ch)
                i += 1
            continue

        name, j = m.group(1), i + m.end()
        # \\ldots and friends: no argument, direct substitution.
        literal = dict(SIMPLE_REPLACEMENTS).get("\\" + name)
        if literal is not None and (j >= len(src) or src[j] != "{"):
            buf.append(literal)
            i = j
            continue

        arg = None
        if j < len(src) and src[j] == "{":
            arg, j = _read_group(src, j)

        if name in DROP_MACROS:
            pass
        elif arg is None:
            buf.append(" ")
        elif name in CODE_MACROS:
            flush()
            out.append(_inline_code(arg))
        elif name in STRONG_MACROS:
            flush()
            out.append("**" + latex_to_markdown(arg) + "**")
        elif name in EMPH_MACROS:
            flush()
            out.append("*" + latex_to_markdown(arg) + "*")
        else:
            buf.append(arg)
        i = j

    flush()
    text = "".join(out)

    # Typographic leftovers, applied after macro expansion so that a `---`
    # inside \py{} has already been protected by the code span above.
    text = text.replace("``", "\u201c").replace("''", "\u201d")
    text = re.sub(r"(?<!-)---(?!-)", "\u2014", text)
    text = re.sub(r"(?<!-)--(?!-)", "\u2013", text)
    text = text.replace("~", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def math_to_text(src: str) -> str:
    """Render one inline-math span as plain Unicode text.

    Deliberately narrow. It covers the symbols and single-level superscripts
    the book actually uses and nothing else; anything more elaborate should be
    noticed rather than silently half-rendered, which is what the leftover
    backslash check at the end is for.
    """
    # `$^\circ$C` for degrees Celsius is the one construct where the caret is
    # part of the symbol rather than a superscript, so it is consumed here
    # before the generic passes can turn it into a stray `^°`.
    out = re.sub(r"\^\s*\{?\\circ\}?", "°", src)
    for macro, char in sorted(MATH_SYMBOLS.items(), key=lambda kv: -len(kv[0])):
        out = re.sub(re.escape(macro) + r"(?![a-zA-Z])", char, out)
    out = re.sub(r"\^\{([0-9+\-n]+)\}", lambda m: m.group(1).translate(SUPERSCRIPTS), out)
    out = re.sub(r"\^([0-9+\-n])", lambda m: m.group(1).translate(SUPERSCRIPTS), out)
    out = out.replace("{", "").replace("}", "")
    out = re.sub(r"\s+", " ", out).strip()
    if "\\" in out:
        print(f"warning: unhandled math macro in {src!r} -> {out!r}", file=sys.stderr)
    return out


def _inline_code(code: str) -> str:
    """Wrap `code` in the shortest backtick fence that can contain it."""
    runs = [len(r) for r in re.findall(r"`+", code)]
    fence = "`" * ((max(runs) + 1) if runs else 1)
    pad = " " if code.startswith("`") or code.endswith("`") else ""
    return f"{fence}{pad}{code}{pad}{fence}"


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

@dataclass
class Exercise:
    number: str          # "5.1.1"
    chapter: int
    group: int
    index: int
    title: str           # Markdown
    prompt: str          # Markdown
    code: str            # Python


@dataclass
class Solution:
    number: str
    chapter: int
    group: int
    title: str
    bug_type: str        # "Logical" | "Runtime" | "Syntax" | ...
    explanation: str     # Markdown
    code: str            # Python


def _split_blocks(body: str, head: re.Pattern) -> list[tuple[re.Match, str]]:
    """Split `body` at each `\\paragraph{...}` heading matched by `head`."""
    starts = [m for m in head.finditer(body)]
    blocks = []
    for n, m in enumerate(starts):
        end = starts[n + 1].start() if n + 1 < len(starts) else len(body)
        blocks.append((m, body[m.start():end]))
    return blocks


def _title_and_rest(block: str) -> tuple[str, str]:
    """Return the heading's title text and everything after the heading."""
    brace = block.index("{")
    inner, after = _read_group(block, brace)
    title = inner.split(" --- ", 1)[1]
    return latex_to_markdown(title), block[after:]


def parse_exercises(manuscript: Path) -> list[Exercise]:
    found: list[Exercise] = []
    for name in CHAPTER_SOURCES:
        text = (manuscript / name).read_text(encoding="utf-8")
        marker = text.find(r"\section{Find the Bug Exercises}")
        if marker < 0:
            continue
        body = text[marker:]
        for head, block in _split_blocks(body, EXERCISE_HEAD):
            number, chapter, group, index = head.group(1, 2, 3, 4)
            title, rest = _title_and_rest(block)
            code_match = MINTED.search(rest)
            if not code_match:
                sys.exit(f"error: exercise {number} in {name} has no python listing")
            prompt = rest[:code_match.start()]
            prompt = re.sub(r"\\label\{ex:[^}]*\}", "", prompt)
            found.append(Exercise(
                number=number, chapter=int(chapter), group=int(group), index=int(index),
                title=title,
                prompt=latex_to_markdown(prompt),
                code=code_match.group(1).rstrip(),
            ))
    return found


def parse_solutions(manuscript: Path) -> list[Solution]:
    text = (manuscript / SOLUTIONS_SOURCE).read_text(encoding="utf-8")
    found: list[Solution] = []
    for head, block in _split_blocks(text, SOLUTION_HEAD):
        number, chapter, group = head.group(1), int(head.group(2)), int(head.group(3))
        title, rest = _title_and_rest(block)
        code_match = MINTED.search(rest)
        if not code_match:
            sys.exit(f"error: solution {number} has no python listing")
        prose = rest[:code_match.start()]
        prose = re.sub(r"\\exref\{[^}]*\}\{[^}]*\}", "", prose)

        # "\textbf{Bug type:} Logical. The third section was ..." -- the word
        # after the label is lifted out so the page can badge it, and the rest
        # stays as the explanation.
        bug_type = ""
        bt = re.search(r"\\textbf\{Bug type:\}\s*([A-Za-z/ ]+?)\.", prose)
        if bt:
            bug_type = bt.group(1).strip()
            prose = prose[:bt.start()] + prose[bt.end():]

        found.append(Solution(
            number=number, chapter=chapter, group=group, title=title, bug_type=bug_type,
            explanation=latex_to_markdown(prose),
            code=code_match.group(1).rstrip(),
        ))
    return found


def parse_group_names(manuscript: Path) -> dict[tuple[int, int], str]:
    """Map (chapter, group) -> topic name, for the chapters that name them."""
    names: dict[tuple[int, int], str] = {}
    text = (manuscript / "python_data_structures.tex").read_text(encoding="utf-8")
    marker = text.find(r"\section{Find the Bug Exercises}")
    for m in SECTION_COMMENT.finditer(text[marker:]):
        names[(5, int(m.group(1)))] = m.group(2)
    return names


# --------------------------------------------------------------------------
# Page generation
# --------------------------------------------------------------------------

def anchor(number: str, prefix: str) -> str:
    return f"{prefix}-{number.replace('.', '-')}"


def group_heading(chapter: int, group: int, members: list,
                  names: dict[tuple[int, int], str], noun: str = "Exercises") -> str:
    """Heading for one group of exercises or solutions.

    Only Chapter 5 names its groups, via the `% Section N: name` comments that
    the manuscript keeps in step between the chapter and the solutions file.
    Everywhere else the range of numbers is used, which is at least accurate --
    inventing topic names for the other eleven chapters would mean guessing at
    what the author grouped them by.
    """
    named = names.get((chapter, group))
    if named:
        return named
    first, last = members[0].number, members[-1].number
    return f"{noun} {first}\u2013{last}" if first != last else f"{noun[:-1]} {first}"


def write_exercise_page(out: Path, chapter: int, items: list[Exercise],
                        names: dict[tuple[int, int], str], order: int) -> None:
    title, slug = CHAPTERS[chapter]
    lines = [
        "---",
        f'title: "Chapter {chapter}: {title}"',
        f'short_title: "Ch. {chapter} \u2014 {title}"',
        "layout: post",
        f"permalink: {PREFIX}/exercises/{slug}/",
        f"order: {order}",
        f"chapter: {chapter}",
        f"exercise_count: {len(items)}",
        "---",
        "",
        f"{len(items)} *Find the Bug* exercises from Chapter {chapter} of "
        f"*Everyday Programming*. Every program below is short, does something "
        f"recognizable, and hides **exactly one** bug \u2014 syntax, runtime, or "
        f"logical. Read it, predict what it does, then run it and find out.",
        "",
        f"Worked solutions for this chapter: "
        f"[Chapter {chapter} solutions]({{{{ site.baseurl }}}}{PREFIX}/solutions/{slug}/). "
        f"Every snippet is also available as a `.py` file \u2014 see "
        f"[Exercises &amp; Solutions]({{{{ site.baseurl }}}}{PREFIX}/book/exercises/).",
        "",
    ]

    by_group: dict[int, list[Exercise]] = {}
    for item in items:
        by_group.setdefault(item.group, []).append(item)

    for group, members in sorted(by_group.items()):
        lines += [f"## {group_heading(chapter, group, members, names)}", ""]
        for ex in members:
            sol_anchor = anchor(ex.number, "sol")
            lines += [
                f"### Exercise {ex.number} \u2014 {ex.title}",
                f"{{: #{anchor(ex.number, 'ex')} }}",
                "",
                ex.prompt,
                "",
                "```python",
                ex.code,
                "```",
                "",
                f"[Solution {ex.number}]({{{{ site.baseurl }}}}{PREFIX}/solutions/{slug}/#{sol_anchor}) "
                f"&middot; [`ex_{ex.number.replace('.', '_')}.py`]"
                f"({{{{ site.baseurl }}}}{PREFIX}/assets/code/exercises/ex_{ex.number.replace('.', '_')}.py)",
                "",
            ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_solution_page(out: Path, chapter: int, items: list[Solution],
                        names: dict[tuple[int, int], str], order: int) -> None:
    title, slug = CHAPTERS[chapter]
    lines = [
        "---",
        f'title: "Chapter {chapter}: {title} \u2014 Solutions"',
        f'short_title: "Ch. {chapter} \u2014 {title}"',
        "layout: post",
        f"permalink: {PREFIX}/solutions/{slug}/",
        f"order: {order}",
        f"chapter: {chapter}",
        "---",
        "",
        f"Worked solutions to the {len(items)} *Find the Bug* exercises in "
        f"[Chapter {chapter}: {title}]({{{{ site.baseurl }}}}{PREFIX}/exercises/{slug}/). "
        f"Each one names the kind of bug, explains why the original misbehaved, "
        f"and shows the corrected program.",
        "",
        "Solutions stay folded until you open them \u2014 try the exercise first; "
        "the diagnosis is where the learning is.",
        "",
    ]

    # Grouped exactly as the exercise page is. Two reasons: the heading levels
    # then run h1 -> h2 -> h3 without a gap, and the sidebar's in-page contents
    # (which lists level 2 only) gets usable entries instead of nothing.
    by_group: dict[int, list[Solution]] = {}
    for item in items:
        by_group.setdefault(item.group, []).append(item)

    for group, members in sorted(by_group.items()):
        lines += [f"## {group_heading(chapter, group, members, names, 'Solutions')}", ""]
        for sol in members:
            stem = sol.number.replace(".", "_")
            lines += [
                f"### Solution {sol.number} \u2014 {sol.title}",
                f"{{: #{anchor(sol.number, 'sol')} }}",
                "",
                '<details markdown="1">',
                "<summary>Show the diagnosis and the fix</summary>",
                "",
            ]
            if sol.bug_type:
                lines += [f"**Bug type:** {sol.bug_type}", ""]
            lines += [
                sol.explanation,
                "",
                "```python",
                sol.code,
                "```",
                "",
                f"[Back to Exercise {sol.number}]"
                f"({{{{ site.baseurl }}}}{PREFIX}/exercises/{slug}/#{anchor(sol.number, 'ex')}) "
                f"&middot; [`sol_{stem}.py`]"
                f"({{{{ site.baseurl }}}}{PREFIX}/assets/code/solutions/sol_{stem}.py)",
                "",
                "</details>",
                "",
            ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _check_header(header: str, name: str) -> None:
    """Fail if a generated docstring header does not parse on its own.

    The exercise code below the header is deliberately allowed to be broken --
    60 of the 445 exercises are syntax bugs, which is the whole point of them --
    so compiling the finished file cannot distinguish "the exercise is meant to
    fail" from "the generator emitted a broken docstring". Compiling the header
    in isolation does, and that is the half this script is responsible for.
    """
    try:
        compile(header + "pass\n", name, "exec")
    except SyntaxError as exc:
        sys.exit(f"error: generated docstring for {name} does not parse "
                 f"(line {exc.lineno}: {exc.msg})")


def write_code_files(root: Path, exercises: list[Exercise],
                     solutions: dict[str, Solution]) -> int:
    """Write one runnable .py per exercise and per solution, plus a zip of all."""
    ex_dir, sol_dir = root / "exercises", root / "solutions"
    for d in (ex_dir, sol_dir):
        shutil.rmtree(d, ignore_errors=True)
        d.mkdir(parents=True)

    written = 0
    for ex in exercises:
        stem = ex.number.replace(".", "_")
        chapter_title = CHAPTERS[ex.chapter][0]
        header = (
            f'"""Exercise {ex.number} \u2014 {_plain(ex.title)}\n\n'
            f"Chapter {ex.chapter}: {chapter_title} \u2014 Everyday Programming\n\n"
            f"{_wrap(_plain(ex.prompt))}\n\n"
            f"This program contains exactly one bug. Solution: sol_{stem}.py\n"
            f'"""\n\n'
        )
        _check_header(header, f"ex_{stem}.py")
        (ex_dir / f"ex_{stem}.py").write_text(header + ex.code + "\n", encoding="utf-8")
        written += 1

        sol = solutions[ex.number]
        sol_header = (
            f'"""Solution {sol.number} \u2014 {_plain(sol.title)}\n\n'
            f"Chapter {sol.chapter}: {chapter_title} \u2014 Everyday Programming\n\n"
            f"Bug type: {sol.bug_type or 'unspecified'}\n\n"
            f"{_wrap(_plain(sol.explanation))}\n\n"
            f"Exercise: ex_{stem}.py\n"
            f'"""\n\n'
        )
        _check_header(sol_header, f"sol_{stem}.py")
        (sol_dir / f"sol_{stem}.py").write_text(sol_header + sol.code + "\n", encoding="utf-8")
        written += 1

    archive = root / "everyday-programming-exercises.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.txt", ZIP_README)
        for path in sorted(ex_dir.iterdir()) + sorted(sol_dir.iterdir()):
            zf.write(path, f"everyday-programming-exercises/{path.parent.name}/{path.name}")
    return written


ZIP_README = """Everyday Programming -- Find the Bug exercises
Dr. Nobel Khandaker

445 exercises and 445 worked solutions, extracted from the book.

  exercises/ex_<chapter>_<group>_<n>.py   the program with the bug in it
  solutions/sol_<chapter>_<group>_<n>.py  the diagnosis and the corrected program

Almost every program runs on a stock CPython 3 with nothing installed:

  python3 exercises/ex_5_1_1.py

Two sets need more. Chapter 17 (testing) uses pytest. Section 13.2 imports
modules such as `conversions` and `shapes` that you are meant to have written
yourself -- those exercises are about the import mechanism, so they raise
ModuleNotFoundError until you create the module beside them.

Some exercises are meant to fail -- a syntax error or an exception is the
bug you are looking for. Read the docstring at the top of each file for what
the program was supposed to do.

Online, with links between each exercise and its solution:
https://intuitai.org/ep/
"""


def _plain(markdown: str) -> str:
    """Strip the Markdown a docstring has no use for, and make it safe to embed.

    The escaping is load-bearing, not defensive. Chapter 10's docstring
    exercises discuss triple quotes in prose -- "opened with \"\"\" but never
    closed" -- and dropping that verbatim into a \"\"\"...\"\"\" header ends the
    header at the quoted example and leaves the remaining prose as code. A
    trailing quote is escaped for the same reason: it would otherwise fuse with
    the closing delimiter into a four-quote run.
    """
    text = re.sub(r"\\([*_\[\]<>])", r"\1", markdown)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return text[:-1] + '\\"' if text.endswith('"') else text


def _wrap(text: str, width: int = 72) -> str:
    import textwrap
    return "\n".join(textwrap.wrap(text, width)) or text


# --------------------------------------------------------------------------

def main() -> int:
    global PREFIX
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", type=Path,
                        default=Path("../manuscripts/everyday-programming"),
                        help="path to the everyday-programming LaTeX sources")
    parser.add_argument("--site", type=Path, default=Path("."),
                        help="path to the site root")
    parser.add_argument("--prefix", default=PREFIX,
                        help="URL path the book is served under, no trailing "
                             f"slash (default: {PREFIX})")
    args = parser.parse_args()
    PREFIX = args.prefix.rstrip("/")

    manuscript = args.manuscript.expanduser().resolve()
    site = args.site.expanduser().resolve()
    if not (manuscript / SOLUTIONS_SOURCE).exists():
        sys.exit(f"error: {manuscript} does not look like the manuscript "
                 f"({SOLUTIONS_SOURCE} not found)")

    exercises = parse_exercises(manuscript)
    solutions = parse_solutions(manuscript)
    names = parse_group_names(manuscript)

    # Invariants. Each is a real property of the manuscript today; if the book
    # changes shape, failing here is the point.
    problems = []
    if len(exercises) != EXPECTED_TOTAL:
        problems.append(f"parsed {len(exercises)} exercises, expected {EXPECTED_TOTAL}")
    if len(solutions) != EXPECTED_TOTAL:
        problems.append(f"parsed {len(solutions)} solutions, expected {EXPECTED_TOTAL}")

    by_number = {s.number: s for s in solutions}
    if len(by_number) != len(solutions):
        problems.append("duplicate solution numbers")
    ex_numbers = {e.number for e in exercises}
    if len(ex_numbers) != len(exercises):
        problems.append("duplicate exercise numbers")
    orphan_ex = sorted(ex_numbers - set(by_number))
    orphan_sol = sorted(set(by_number) - ex_numbers)
    if orphan_ex:
        problems.append(f"exercises with no solution: {orphan_ex}")
    if orphan_sol:
        problems.append(f"solutions with no exercise: {orphan_sol}")
    unknown = sorted({e.chapter for e in exercises} - set(CHAPTERS))
    if unknown:
        problems.append(f"exercises in chapters absent from CHAPTERS: {unknown}")
    empty = [e.number for e in exercises if not e.code.strip()]
    if empty:
        problems.append(f"exercises with an empty listing: {empty}")
    if problems:
        for p in problems:
            print(f"error: {p}", file=sys.stderr)
        return 1

    ex_dir = site / "_exercises"
    sol_dir = site / "_solutions"
    for d in (ex_dir, sol_dir):
        shutil.rmtree(d, ignore_errors=True)
        d.mkdir(parents=True)

    by_chapter: dict[int, list[Exercise]] = {}
    for ex in exercises:
        by_chapter.setdefault(ex.chapter, []).append(ex)

    for order, chapter in enumerate(sorted(by_chapter), start=1):
        items = sorted(by_chapter[chapter], key=lambda e: (e.group, e.index))
        slug = CHAPTERS[chapter][1]
        write_exercise_page(ex_dir / f"{slug}.md", chapter, items, names, order)
        write_solution_page(sol_dir / f"{slug}.md", chapter,
                            [by_number[e.number] for e in items], names, order)

    written = write_code_files(site / "assets" / "code", exercises, by_number)

    # The download button quotes the archive's size. Publishing it as data keeps
    # the page from drifting when the exercise set changes.
    archive = site / "assets" / "code" / "everyday-programming-exercises.zip"
    size = archive.stat().st_size
    data = site / "_data" / "downloads.yml"
    data.parent.mkdir(parents=True, exist_ok=True)
    # How the 445 bugs break down by kind. Published on the exercises page, so
    # it is counted from the solutions rather than asserted in prose.
    kinds: dict[str, int] = {}
    for sol in solutions:
        kinds[sol.bug_type or "unspecified"] = kinds.get(sol.bug_type or "unspecified", 0) + 1

    data.write_text(
        "# Generated by tools/extract_exercises.py. Do not edit by hand.\n"
        f"exercise_zip_bytes: {size}\n"
        f"exercise_zip_size: \"{size / 1024:.0f} KB\"\n"
        f"exercise_count: {len(exercises)}\n"
        f"program_count: {written}\n"
        "bug_kinds:\n"
        + "".join(f"  {k.lower().replace('/', '_')}: {v}\n"
                  for k, v in sorted(kinds.items(), key=lambda kv: -kv[1])),
        encoding="utf-8")

    print(f"{len(exercises)} exercises and {len(solutions)} solutions "
          f"across {len(by_chapter)} chapters")
    print(f"  _exercises/  {len(by_chapter)} pages")
    print(f"  _solutions/  {len(by_chapter)} pages")
    print(f"  assets/code/ {written} .py files + everyday-programming-exercises.zip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
