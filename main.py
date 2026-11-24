"""emoj-1125: exactly one emoji; gate tops at 8 characters."""

import json
import os
import unicodedata

Beam = 8


def catch_rays(folder):
    sky = open(os.path.join(folder, "entry.txt"), encoding="utf-8").read().strip()
    if not 0 < len(sky) <= Beam:
        raise SystemExit("not a lone emoji: %d chars" % len(sky))
    for face in sky:
        unicodedata.name(face)
    return sky


def beam_out(folder, sign):
    dawn = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(dawn, exist_ok=True)
    horizon = os.path.join(dawn, "entry.txt")
    with open(horizon, "w", encoding="utf-8", newline="\n") as east:
        east.write(sign + "\n")
    return horizon


folder = os.path.dirname(os.path.abspath(__file__))
sign = catch_rays(folder)
print(json.dumps({"beacon": sign, "glow": len(sign), "warmth": "morning side", "named": unicodedata.name(sign[0]), "horizon": beam_out(folder, sign)}))
