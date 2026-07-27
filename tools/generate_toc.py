#!/usr/bin/env python3
"""Turn a book's LaTeX table of contents into a _data/*.yml file.

Emitting data rather than a finished page keeps the contents listing and the
prose that introduces it apart: the table-of-contents page owns the words and
loops over what this writes. Re-run after a rebuild of the book.

Both books on this domain are typeset with sicp-style.tex, so both emit the
same `\\contentsline` grammar and one parser serves them. The defaults are
Everyday Programming's; Everyday AI passes its own:

    ./tools/generate_toc.py --manuscript ../manuscripts/everyday-programming

    ./tools/generate_toc.py --manuscript ../manuscripts/everyday-ai \\
        --stem everyday-ai --out eai/toc.yml --min-chapters 7

--out is a path under _data/, so a nested name is allowed and is what the
second book uses. It has to be: Liquid would read `site.data.eai-toc` as a
subtraction, whereas `_data/eai/toc.yml` reaches the page as
`site.data.eai.toc`.

--min-chapters is a floor, not a count: it exists so that a .toc truncated by
a failed LaTeX run is caught here rather than silently shipping half a
contents listing. Raise it when a book grows.

It counts NUMBERED chapters only. Both books' .toc files end with an unnumbered
`Index` entry, which is parsed and kept -- the contents page renders it -- but
counting it would inflate the total by one and let the floor pass with a real
chapter missing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from extract_exercises import _read_group, latex_to_markdown  # noqa: E402

CONTENTSLINE = re.compile(r"\\contentsline \{(part|chapter|section)\}\{")

# minted's inline macro survives into the .toc in its fully expanded,
# write-safe form. Collapsing it back to \mintinline lets the shared converter
# handle it, so `\py{if}` in a section title reaches the page as `if` in code
# style rather than as a wall of FVExtra internals.
FVEXTRA = r"\FVExtraRobustCommand \RobustMintInline \FVExtraAlwaysUnexpanded "
FVEXTRA_INNER = r"\FVExtraUnexpandedReadStarOArgMArgBVArg "


def normalise_minted(src: str) -> str:
    out, i = [], 0
    while True:
        j = src.find(FVEXTRA, i)
        if j < 0:
            out.append(src[i:])
            return "".join(out)
        out.append(src[i:j])
        group, after = _read_group(src, j + len(FVEXTRA))
        inner = group.strip()
        if inner.startswith(FVEXTRA_INNER.strip()):
            rest = inner[len(FVEXTRA_INNER.strip()):].lstrip()
            k = _read_group(rest, 0)[1]      # skip the {python} language argument
            code = _read_group(rest, k)[0]
            out.append("\\mintinline{python}{" + code + "}")
        else:
            out.append(inner)
        i = after


def clean(title: str) -> str:
    title = normalise_minted(title)
    title = re.sub(r"\\xpg@aux \{[^}]*\}\{[^}]*\}", "", title)
    title = re.sub(r"\\hspace \{[^}]*\}", " ", title)
    return latex_to_markdown(title)


def parse_toc(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    parts: list[dict] = []
    current_chapter: dict | None = None

    for match in CONTENTSLINE.finditer(text):
        kind = match.group(1)
        body, after = _read_group(text, match.end() - 1)
        page_str, _ = _read_group(text, after)

        number = ""
        num = re.match(r"\\numberline \{([^}]*)\}", body)
        if num:
            number, body = num.group(1), body[num.end():]

        title = clean(body)
        try:
            page = int(page_str)
        except ValueError:
            # Roman-numeral front matter: a Preface is numbered vi, not 6. It
            # is dropped rather than rendered, since a contents listing of
            # chapters has no room for it.
            #
            # current_chapter has to be cleared too. Without that, a dropped
            # chapter leaves the PREVIOUS chapter current, and any section
            # belonging to the dropped one is then filed under it -- silently,
            # and only in the front matter, which is exactly where nobody
            # looks. Neither book triggers this today (Everyday AI's preface
            # has no sections, and Everyday Programming's .toc has no such
            # entry at all), but that preface is still lorem ipsum and will be
            # rewritten.
            if kind in ("part", "chapter"):
                current_chapter = None
            continue

        if kind == "part":
            # Parts carry their numeral inside the title: "I\hspace{1em}Basic
            # Concepts". Split it back off so the page can style the two.
            numeral, _, name = title.partition(" ")
            parts.append({"part": numeral.strip(), "title": name.strip() or numeral,
                          "page": page, "chapters": []})
            current_chapter = None
        elif kind == "chapter":
            if not parts:
                parts.append({"part": "", "title": "", "page": page, "chapters": []})
            current_chapter = {"number": number, "title": title,
                               "page": page, "sections": []}
            parts[-1]["chapters"].append(current_chapter)
        elif kind == "section" and current_chapter is not None:
            current_chapter["sections"].append(
                {"number": number, "title": title, "page": page})
    return parts


def yaml_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render(parts: list[dict], stem: str) -> str:
    lines = [
        f"# Generated by tools/generate_toc.py from {stem}.toc.",
        "# Do not edit by hand; re-run the script after rebuilding the book.",
    ]
    for part in parts:
        lines += [
            f"- part: {yaml_escape(part['part'])}",
            f"  title: {yaml_escape(part['title'])}",
            f"  page: {part['page']}",
            "  chapters:",
        ]
        for ch in part["chapters"]:
            lines += [
                f"    - number: {yaml_escape(ch['number'])}",
                f"      title: {yaml_escape(ch['title'])}",
                f"      page: {ch['page']}",
            ]
            if ch["sections"]:
                lines.append("      sections:")
                for sec in ch["sections"]:
                    lines += [
                        f"        - number: {yaml_escape(sec['number'])}",
                        f"          title: {yaml_escape(sec['title'])}",
                        f"          page: {sec['page']}",
                    ]
            else:
                lines.append("      sections: []")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", type=Path,
                        default=Path("../manuscripts/everyday-programming"))
    parser.add_argument("--site", type=Path, default=Path("."))
    parser.add_argument("--stem", default="everyday-programming",
                        help="basename of the .toc file, without the extension")
    parser.add_argument("--out", default="toc.yml",
                        help="filename to write under _data/")
    parser.add_argument("--min-chapters", type=int, default=20,
                        help="fail if fewer chapters than this are parsed")
    args = parser.parse_args()

    toc = args.manuscript.expanduser().resolve() / f"{args.stem}.toc"
    if not toc.exists():
        sys.exit(f"error: {toc} not found -- build the book first")

    parts = parse_toc(toc)
    chapters = sum(len(p["chapters"]) for p in parts)
    sections = sum(len(c["sections"]) for p in parts for c in p["chapters"])
    numbered = sum(1 for p in parts for c in p["chapters"] if c["number"])
    if numbered < args.min_chapters:
        sys.exit(f"error: only {numbered} numbered chapters parsed "
                 f"(of {chapters} entries); the .toc looks incomplete")

    site_root = args.site.expanduser().resolve()
    out = (site_root / "_data" / args.out).resolve()
    # --out is documented as a path under _data/, and a nested one is what the
    # second book passes. Anything that escapes _data/ is a typo rather than an
    # intention, and without this it would be written first and only noticed at
    # the relative_to() below, after the damage.
    if not out.is_relative_to(site_root / "_data"):
        sys.exit(f"error: --out must stay under _data/; {args.out!r} resolves "
                 f"to {out}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(parts, args.stem), encoding="utf-8")

    last = max(c["page"] for p in parts for c in p["chapters"])
    print(f"{len(parts)} parts, {chapters} chapters, {sections} sections "
          f"-> {out.relative_to(args.site.expanduser().resolve())} (last page {last})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
