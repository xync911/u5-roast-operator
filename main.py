"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one line roasting our own human operator, at most
140 characters, savage in wording but affectionate at heart.
He types 'just one more thing' at 3 a.m. like sleep is a bug
he can fix in the next sprint. The roast is the schedule itself.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
