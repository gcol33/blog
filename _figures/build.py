"""Render every figure script in this directory.

    python _figures/build.py              # all figures
    python _figures/build.py dark-forest  # scripts whose name contains a term
"""

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKIP = {"build.py", "style.py"}

sys.path.insert(0, str(HERE))
terms = sys.argv[1:]

for script in sorted(HERE.glob("*.py")):
    if script.name in SKIP:
        continue
    if terms and not any(t in script.stem for t in terms):
        continue
    runpy.run_path(str(script), run_name="__main__")
