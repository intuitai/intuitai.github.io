#!/usr/bin/env python3
r"""Build the free Chapters 1-2 sample PDF of "Everyday AI".

    ./tools/build_eai_sample.py --manuscript ../manuscripts/everyday-ai

The sample is a real XeLaTeX build, not pages carved out of everyday-ai.pdf
with Ghostscript, because four things have to change before the file is fit to
publish:

  * the DRAFT watermark comes off,
  * the preface is dropped -- it is still lorem ipsum in the manuscript,
  * the ISBN comes off the copyright page -- the manuscript still carries
    LaTeX's example number, 978-3-16-148410-0, flagged in everyday-ai.tex with
    "replace this with your own ISBN". Shipping it would hand every reader a
    false identifier for the book, and unlike the watermark it is not obviously
    placeholder text to the person reading it, and
  * chapters 3-7 and the index go, which is what makes it a sample.

Page numbers DO match the printed book, and the site copy may say so. \mainmatter
resets to arabic 1 after the front matter, so dropping the preface moves the
physical position of Chapter 1 in the file without changing its printed number:
Chapter 1 is page 1 and Chapter 2 is page 7 in both this sample and the full
everyday-ai.pdf. (An earlier version of this docstring claimed the opposite and
the site copy repeated it. Verified entry by entry against everyday-ai.toc.)

The manuscript is copied to a temporary directory first, so a build here never
writes into the author's repository -- not even the .aux and .toc files that a
LaTeX run normally leaves behind.

Every edit below is an EXACT string that must appear EXACTLY ONCE in its file.
That is deliberate, and it matches extract_exercises.py: when the manuscript is
reorganised, this should fail loudly rather than quietly ship a sample with the
watermark still on it, or the placeholder ISBN still in it. If it raises, look
at what actually changed and update the edit -- do not loosen it into a regex.

Requires XeLaTeX and biber on PATH, and the three OpenType families
sicp-style.tex selects installed system-wide (`make fontcheck` in the
manuscript checks them).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

STEM = "everyday-ai"

# Copied into the build directory. The manuscript also holds build products,
# a .claude directory and the 1.6 MB cover artwork's siblings; none of that is
# needed to typeset two chapters.
SOURCES = ["everyday-ai.tex", "sicp-style.tex", "references.bib"]
SOURCE_DIRS = ["frontmatter", "content", "images"]

# (file, what it is, exact text, replacement). See the module docstring on why
# these are exact strings rather than patterns.
EDITS = [
    (
        "everyday-ai.tex",
        "the DRAFT watermark",
        "% Watermark. Remove this block for a finished-looking PDF.\n"
        "\\usepackage{draftwatermark}\n"
        "\\SetWatermarkText{DRAFT}\n"
        "\\SetWatermarkScale{1}\n"
        "\\SetWatermarkColor[gray]{0.9}\n"
        "\\SetWatermarkAngle{45}\n",
        "% Watermark removed by tools/build_eai_sample.py.\n",
    ),
    (
        "everyday-ai.tex",
        "the preface (still lorem ipsum in the manuscript)",
        "\\input{frontmatter/preface}\n",
        "% Preface omitted from the sample by tools/build_eai_sample.py.\n",
    ),
    (
        "everyday-ai.tex",
        "chapters 3 to 7",
        "\\input{content/chapter3}\n"
        "\\input{content/chapter4}\n"
        "\\input{content/chapter5}\n"
        "\\input{content/chapter6}\n"
        "\\input{content/chapter7}\n",
        "% Chapters 3-7 omitted from the sample by tools/build_eai_sample.py.\n",
    ),
    (
        "everyday-ai.tex",
        "the index",
        "\\printindex\n",
        "% Index omitted from the sample by tools/build_eai_sample.py.\n",
    ),
    (
        # Not \bookISBN in the master: blanking the macro would leave the
        # "ISBN" label standing on its own with nothing after it. The whole
        # line has to go, and the line lives on the copyright page.
        "frontmatter/copyrightpage.tex",
        "the placeholder ISBN",
        "\\par \\acronym{ISBN} \\bookISBN\n",
        "% ISBN omitted from the sample by tools/build_eai_sample.py: the\n"
        "% manuscript still carries LaTeX's example number.\n",
    ),
]


def apply_edits(build: Path) -> None:
    for name, what, old, new in EDITS:
        path = build / name
        text = path.read_text(encoding="utf-8")
        found = text.count(old)
        if found != 1:
            # Print the string that was looked for. Without it, a trailing
            # space, an inserted blank line and a genuine reorganisation all
            # produce the identical "found it 0 times" and you have to open
            # this file to find out what was even being matched.
            shown = old if len(old) <= 400 else old[:400] + "\n[...]"
            sys.exit(
                f"error: expected to find {what} exactly once in {name}, "
                f"found it {found} times.\n"
                f"       The manuscript has changed. Update EDITS in "
                f"{Path(__file__).name} deliberately rather than relaxing it.\n"
                f"       Looked for, exactly:\n"
                + "".join(f"       | {line}\n" for line in shown.splitlines())
            )
        path.write_text(text.replace(old, new), encoding="utf-8")


def stage(manuscript: Path, build: Path) -> None:
    for name in SOURCES:
        src = manuscript / name
        if not src.exists():
            sys.exit(f"error: {src} not found")
        shutil.copy2(src, build / name)
    for name in SOURCE_DIRS:
        src = manuscript / name
        if not src.is_dir():
            sys.exit(f"error: {src} not found")
        shutil.copytree(src, build / name)

    apply_edits(build)


class KeepBuildDir(Exception):
    """A failure whose diagnosis is inside the build directory.

    Raised instead of calling sys.exit so that main() can leave the directory
    on disk and say where it is: when xelatex or biber fails, the .log and .blg
    files it wrote are the whole diagnosis, and deleting them is the one thing
    that must not happen.
    """


def require_tools() -> None:
    """Fail with a sentence rather than a traceback when TeX is missing.

    Being on a machine with no TeX toolchain is the ORDINARY case for this
    repository -- the generated output is committed precisely so the site
    builds without one -- so `FileNotFoundError: 'xelatex'` out of the middle of
    build_pdf is the wrong way to say it. page_count already takes this care
    over a missing Ghostscript; the two should behave alike.
    """
    missing = [t for t in ("xelatex", "biber") if shutil.which(t) is None]
    if missing:
        sys.exit(
            f"error: {' and '.join(missing)} not found on PATH.\n"
            f"       This script rebuilds the manuscript, so it needs a TeX\n"
            f"       installation and the three OpenType families\n"
            f"       sicp-style.tex selects. Nothing else in this repository\n"
            f"       does -- the sample PDF is committed, so the site builds\n"
            f"       without TeX. Skip this script unless the sample itself\n"
            f"       needs regenerating."
        )


def run(cmd: list[str], build: Path) -> None:
    done = subprocess.run(cmd, cwd=build, capture_output=True, text=True)
    if done.returncode != 0:
        # Both streams, not just stdout. XeLaTeX puts its error text on stdout
        # and -halt-on-error leaves it at the very end, but biber reports on
        # stderr -- and biber is the step most likely to fail here, on a stale
        # PAR cache. Reporting stdout alone made that failure look like silence.
        tail = "\n".join((done.stdout + done.stderr).splitlines()[-40:])
        # KeepBuildDir, not sys.exit: main()'s `finally` would otherwise delete
        # the build directory on the way out, taking everyday-ai.log and
        # everyday-ai.blg with it -- and biber's .blg is where the cause
        # actually is when biber is what failed.
        raise KeepBuildDir(f"error: {cmd[0]} failed in {build}\n{tail}")


def build_pdf(build: Path) -> Path:
    # The Makefile's sequence, less its makeindex step: xelatex -> biber ->
    # xelatex -> xelatex. Two passes after biber are what fill in the table of
    # contents, the list of figures and the footnoted citations; one is not
    # enough. makeindex is dropped because the sample excises \printindex, and
    # sicp-style's imakeidx shells out to it anyway under --shell-escape.
    xelatex = ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
               "--shell-escape", f"{STEM}.tex"]
    run(xelatex, build)
    run(["biber", STEM], build)
    run(xelatex, build)
    run(xelatex, build)

    pdf = build / f"{STEM}.pdf"
    if not pdf.exists():
        sys.exit(f"error: {pdf} was not produced")
    return pdf


def page_count(pdf: Path) -> int | None:
    """Page count via Ghostscript, or None if gs is not installed.

    Only used for the summary line and the sanity check below, so a missing
    Ghostscript is not worth failing the build over.
    """
    try:
        done = subprocess.run(
            ["gs", "-q", "-dNODISPLAY", "-dNOSAFER", "-c",
             f"({pdf}) (r) file runpdfbegin pdfpagecount = quit"],
            capture_output=True, text=True, check=True)
        return int(done.stdout.strip())
    except (OSError, subprocess.CalledProcessError, ValueError):
        return None


def check_contents(build: Path) -> None:
    r"""Fail unless the sample contains exactly chapters 1 and 2.

    A page count alone is a poor guard. It catches a sample that is too long --
    an excision that silently stopped matching -- but says nothing about one
    that is too SHORT, and a sample missing Chapter 2 would have sailed through
    a `pages > 40` test at 7 pages.

    The build's own .toc is the precise check, and it is free: LaTeX has just
    written down exactly which chapters it typeset. Front matter does not
    appear (\chapter* writes no \numberline) and neither does the index, so the
    numbered chapters are all that is left.
    """
    toc = build / f"{STEM}.toc"
    if not toc.exists():
        sys.exit(f"error: {toc} was not written; cannot verify the sample's contents")

    numbers = re.findall(r"\\contentsline \{chapter\}\{\\numberline \{([^}]*)\}",
                         toc.read_text(encoding="utf-8"))
    if numbers != ["1", "2"]:
        sys.exit(
            f"error: the sample contains chapters {numbers or '[none]'}, "
            f"expected exactly ['1', '2'].\n"
            f"       Either an excision in EDITS matched more than it should, "
            f"or a chapter failed to typeset."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", type=Path,
                        default=Path("../manuscripts/everyday-ai"))
    parser.add_argument("--site", type=Path, default=Path("."))
    parser.add_argument("--keep", action="store_true",
                        help="leave the build directory in place for inspection")
    args = parser.parse_args()

    manuscript = args.manuscript.expanduser().resolve()
    site = args.site.expanduser().resolve()
    if not (manuscript / f"{STEM}.tex").exists():
        sys.exit(f"error: {manuscript}/{STEM}.tex not found -- pass --manuscript")
    require_tools()

    keep = args.keep
    build = Path(tempfile.mkdtemp(prefix="eai-sample-"))
    try:
        stage(manuscript, build)
        pdf = build_pdf(build)

        check_contents(build)

        # Bounds either side, now that check_contents has confirmed WHICH
        # chapters are present: this catches a chapter that typeset but came
        # out mangled, in a way a chapter list cannot.
        pages = page_count(pdf)
        if pages is not None and not 12 <= pages <= 40:
            sys.exit(f"error: the sample came out at {pages} pages; expected "
                     f"12 to 40. Chapters 1 and 2 plus front matter is 19.")

        out = site / "eai" / "assets" / "pdf" / "everyday-ai-sample-chapters-1-2.pdf"
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, out)

        size = out.stat().st_size
        print(f"{out.relative_to(site)}  "
              f"{'' if pages is None else str(pages) + ' pages, '}"
              f"{size / 1024 / 1024:.1f} MB")
    except KeepBuildDir as failure:
        keep = True
        print(failure, file=sys.stderr)
        print(f"\n  {STEM}.log  xelatex's log\n"
              f"  {STEM}.blg  biber's log -- look here first if biber failed",
              file=sys.stderr)
        return 1
    finally:
        if keep:
            print(f"build directory kept at {build}", file=sys.stderr)
        else:
            shutil.rmtree(build, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
