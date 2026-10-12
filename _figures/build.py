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

from style import OverlapError  # noqa: E402

failed = []
for script in sorted(HERE.glob("*.py")):
    if script.name in SKIP:
        continue
    if terms and not any(t in script.stem for t in terms):
        continue
    try:
        runpy.run_path(str(script), run_name="__main__")
    except OverlapError as err:
        print(err, file=sys.stderr)
        failed.append(script.stem)

if failed:
    sys.exit(f"overlapping text in: {', '.join(failed)}")
