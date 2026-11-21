#!/usr/bin/env python3
# Copyright (C) 2026 Edmund Paulino Valdez
# License: AGPL-3.0-or-later
"""Automated build-time audit for LXX-Strongs-and-Morph-Codes modules, README.md, and LICENSE."""

import glob, os, sqlite3, sys

REQUIRED_DOC_TOKENS = [
    ("AGPL-3.0-or-later", ["agpl-3.0-or-later"]),
    ("Brenton", ["brenton"]),
    ("Steve (mathetes)", ["mathetes"]),
    ("communitychaplainfellowship.org", ["communitychaplainfellowship.org"]),
    ("CATSS / CCAT non-commercial", ["catss", "non-commercial"]),
    ("Rúbio Terra / lxxmorph-rc", ["lxxmorph-rc"]),
    ("eliranwong/LXX-Rahlfs-1935 (CC BY-NC-SA 4.0)", ["lxx-rahlfs-1935", "cc by-nc-sa 4.0"]),
    ("eliranwong/LXX-Swete-1930 (GPL-3.0)", ["lxx-swete-1930", "gpl-3.0"]),
    ("sleeptillseven/LXX-Swete", ["sleeptillseven/lxx-swete"]),
    ("STEPBible TVTMS (CC BY 4.0)", ["stepbible", "cc by 4.0"]),
    ("Maurice A. Robinson (RMAC)", ["robinson"]),
    ("David W. Packard (PMAD)", ["packard"]),
    ("Costas Stergiou", ["costas stergiou"]),
]

def latest(pattern):
    matches = sorted(glob.glob(pattern))
    if not matches: raise FileNotFoundError(f"No files matching {pattern}")
    return matches[-1]

errors = []
for doc in ("README.md", "LICENSE"):
    if not os.path.isfile(doc):
        errors.append(f"[MISSING_FILE] {doc} not found")
        continue
    low = open(doc, encoding="utf-8").read().lower()
    for label, toks in REQUIRED_DOC_TOKENS:
        for tok in toks:
            if tok not in low:
                errors.append(f"[DOC_PARITY] {doc} missing '{tok}' ({label})")

for prefix, must_have in [
    ("modules/LXX_Brenton_*.ot", ["copyright=", "mathetes", "communitychaplainfellowship.org", "lxxmorph-rc", "gbl-epv"]),
    ("modules/LXX_Rahlfs_*.ot", ["copyright=", "lxx-rahlfs-1935", "cc by-nc-sa 4.0", "non-commercial", "gbl-epv"]),
    ("modules/SweteLXX_*.ot", ["copyright=", "lxx-swete-1930", "gpl-3.0", "sleeptillseven/lxx-swete", "stepbible", "gbl-epv"]),
]:
    path = latest(prefix)
    raw = open(path, "rb").read()
    if not raw.startswith(b"\xef\xbb\xbf"): errors.append(f"[BOM] {path} missing UTF-8 BOM")
    lines = raw.decode("utf-8-sig").splitlines()
    if len(lines) < 23145: errors.append(f"[LINES] {path} has only {len(lines)} lines")
    footer = "\n".join(lines[23145:]).lower()
    if "epv-thayer-kjv_dct.twm" in footer: errors.append(f"[STALE_REF] {path} still references epv-thayer-kjv_dct.twm")
    for tok in must_have:
        if tok not in footer: errors.append(f"[OT_ATTRIBUTION] {path} footer missing '{tok}'")

dct_path = latest("modules/Packard_s_and_Robinson_s_Morphological_Analysis_Codes_dct_*.dct.twm")
con = sqlite3.connect(dct_path)
cur = con.cursor()
if cur.execute("PRAGMA integrity_check").fetchone()[0] != "ok": errors.append(f"[INTEGRITY] {dct_path}")
cfg = {k: (v.decode("latin1") if isinstance(v, bytes) else str(v)) for k, v in cur.execute("SELECT name, value FROM config").fetchall()}
if "packard" not in cfg.get("author", "").lower() or "robinson" not in cfg.get("author", "").lower():
    errors.append(f"[DCT_AUTHOR] {dct_path} config.author missing Robinson/Packard")
about_low = cfg.get("about", "").lower()
if "offical" in about_low: errors.append(f"[DCT_TYPO] {dct_path} config.about contains 'offical'")
for tok in ("packard", "robinson", "catss", "non-commercial", "agpl-3.0-or-later"):
    if tok not in about_low: errors.append(f"[DCT_ABOUT] {dct_path} config.about missing '{tok}'")
con.close()

if errors:
    for e in errors: print(e)
    sys.exit(1)
print("AUDIT PASSED: 0 issues across LICENSE, README.md, 3 .ot modules, and RMAC/PMAD .dct.twm.")
