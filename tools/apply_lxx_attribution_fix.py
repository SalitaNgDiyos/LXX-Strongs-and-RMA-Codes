#!/usr/bin/env python3
# Copyright (C) 2026 Edmund Paulino Valdez
# License: AGPL-3.0-or-later
"""Apply attribution, copyright, and companion-lexicon metadata updates to LXX modules."""

import shutil, sqlite3, sys

STAMP = "2026-11-21_2015"
BRENTON_SRC = "modules/LXX_Brenton_2026-11-20_2111.ot"
RAHLFS_SRC = "modules/LXX_Rahlfs_2026-11-20_2111.ot"
SWETE_SRC = "modules/SweteLXX_2026-11-20_2111.ot"
DCT_SRC = "modules/Packard_s_and_Robinson_s_Morphological_Analysis_Codes_dct_2026-11-20_2242.dct.twm"

BRENTON_DST = f"modules/LXX_Brenton_{STAMP}.ot"
RAHLFS_DST = f"modules/LXX_Rahlfs_{STAMP}.ot"
SWETE_DST = f"modules/SweteLXX_{STAMP}.ot"
DCT_DST = f"modules/Packard_s_and_Robinson_s_Morphological_Analysis_Codes_dct_{STAMP}.dct.twm"

def patch_brenton():
    text = open(BRENTON_SRC, "r", encoding="utf-8-sig", newline="").read()
    text = text.replace("version.date=2026-11-20", "version.date=2026-11-21", 1)
    if "copyright=" not in text:
        text = text.replace(
            "creator=Edmund Valdez",
            "creator=Edmund Valdez\r\n"
            "source=Brenton (1851/1879, public domain); Steve (mathetes) theWord forum module; communitychaplainfellowship.org; CATSS / lxxmorph-rc (Rubio Terra)\r\n"
            "copyright=Greek text public domain (Brenton 1851/1879). CATSS-derived morphological tagging subject to CCAT non-commercial user agreement.",
            1,
        )
    text = text.replace("<i>EPV Greek Definitions</i> (epv-thayer-kjv_dct.twm)", "<i>The Greek Bible English Lexicons</i> (GBL-EPV, SalitaNgDiyos/The-Greek-Bible-English-Lexicons)")
    text = text.replace("<b>Sources:</b> Brenton's Septuagint (Greek text); the LXX morphological database (lxxmorph);", "<b>Sources:</b> Brenton's Septuagint (1851/1879, public domain); foundational tagged module by Steve (mathetes); CATSS LXX morphological database (University of Pennsylvania, non-commercial) via lxxmorph-rc (Rúbio Terra);", 1)
    open(BRENTON_DST, "w", encoding="utf-8-sig", newline="").write(text)

def patch_rahlfs():
    text = open(RAHLFS_SRC, "r", encoding="utf-8-sig", newline="").read()
    text = text.replace("version.date=2026-11-20", "version.date=2026-11-21", 1)
    text = text.replace(
        "source=CATSS LXX Morphology (lxxmorph), Center for Computer Analysis of Texts, University of Pennsylvania",
        "source=CATSS LXX Morphology (University of Pennsylvania) via lxxmorph-rc (Rúbio Terra); eliranwong/LXX-Rahlfs-1935 (CC BY-NC-SA 4.0)\r\n"
        "copyright=CATSS LXX Morphology (University of Pennsylvania) non-commercial user agreement; eliranwong/LXX-Rahlfs-1935 (CC BY-NC-SA 4.0). Non-commercial use only.",
        1,
    )
    text = text.replace("<i>Bible Greek Definitions</i> (epv-thayer-kjv_dct.twm)", "<i>The Greek Bible English Lexicons</i> (GBL-EPV, SalitaNgDiyos/The-Greek-Bible-English-Lexicons)")
    text = text.replace("as in the LXX Morph module (lxxmorph-rc).", "as in the LXX Morph module (lxxmorph-rc, created by Rúbio Terra).", 1)
    open(RAHLFS_DST, "w", encoding="utf-8-sig", newline="").write(text)

def patch_swete():
    text = open(SWETE_SRC, "r", encoding="utf-8-sig", newline="").read()
    text = text.replace("version.date=2026-11-20", "version.date=2026-11-21", 1)
    text = text.replace("Companion dictionary: EPV Greek Definitions (epv-thayer-kjv_dct.twm).", "Companion dictionary: The Greek Bible English Lexicons (GBL-EPV, SalitaNgDiyos/The-Greek-Bible-English-Lexicons).")
    open(SWETE_DST, "w", encoding="utf-8-sig", newline="").write(text)

def patch_dct():
    shutil.copy2(DCT_SRC, DCT_DST)
    con = sqlite3.connect(DCT_DST)
    cur = con.cursor()
    cur.execute("UPDATE config SET value=? WHERE name='author'", ("Robinson, Maurice A.; Packard, David W. (CATSS); Valdez, Edmund",))
    cur.execute("UPDATE config SET value=? WHERE name='version.date'", ("2026-11-21",))
    about = cur.execute("SELECT value FROM config WHERE name='about'").fetchone()[0]
    if isinstance(about, bytes): about = about.decode("latin1")
    about = about.replace("offical", "official")
    credit = (
        r"\par\par \b Sources & Licenses:\b0  Combines Robinson's Morphological Analysis Codes (RMAC, Dr. Maurice A. Robinson), "
        r"Packard's Morphological Analysis Dictionary (PMAD, David W. Packard / CATSS, University of Pennsylvania, non-commercial user agreement), "
        r"theWord formatting by Costas Stergiou and Rubio Terra, and 2026 canonical/deuterocanonical Septuagint extensions by Edmund Paulino Valdez "
        r"(paired with GBL-EPV). Original build/audit scripts are licensed under AGPL-3.0-or-later.\par"
    )
    i = about.rfind("}")
    cur.execute("UPDATE config SET value=? WHERE name='about'", (about[:i] + credit + about[i:],))
    con.commit()
    assert cur.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    con.close()

patch_brenton(); patch_rahlfs(); patch_swete(); patch_dct()
print(f"Built all 4 updated modules stamped {STAMP}.")
