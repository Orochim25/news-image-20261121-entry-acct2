#!/usr/bin/env python3
"""news-image-20261121 entry for make.fun account 2 (orochim25).

Copies the pre-drawn entry.png (a flat-vector newspaper of Saturday
21 November 2026, drawn by compose_acct2.py) to $MAKEFUN_OUTPUT_DIR.
Standard library only, no network, deterministic bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    with open(SRC, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    if size > 1048576:
        print("entry.png exceeds 1 MiB:", size, file=sys.stderr)
        sys.exit(1)
    print("wrote", dst, size, "bytes")


if __name__ == "__main__":
    main()
