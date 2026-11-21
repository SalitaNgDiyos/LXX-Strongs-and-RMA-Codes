# LXX Strong's and Morphology Codes (theWord Modules)

Fully tagged Greek Old Testament (Septuagint) modules and morphology code dictionary for theWord Bible software (Windows, Linux, Android), keyed to Strong's numbers (`G1–G15737`) and paired with the companion lexicon **The Greek Bible English Lexicons (`GBL-EPV`)** (`SalitaNgDiyos/The-Greek-Bible-English-Lexicons`).

## Included Modules (`modules/`)

| Module | File Pattern | Text Base | Morphology & Tagging |
|---|---|---|---|
| **LXX Brenton+** | `LXX_Brenton_<date>.ot` | Sir Lancelot C. L. Brenton (1851/1879) | Strong's (`G1–G13149`), Packard/Robinson morph codes, lemmas, Brenton verse numbers |
| **LXX Rahlfs+** | `LXX_Rahlfs_<date>.ot` | Alfred Rahlfs (1935) via CATSS / `lxxmorph-rc` + `LXX-Rahlfs-1935` | Strong's (`G1–G13149`), Packard CATSS morph codes, lemmas, CATSS/LXX verse markers |
| **SweteLXX+** | `SweteLXX_<date>.ot` | H. B. Swete (1909–1930) via `LXX-Swete-1930` & `sleeptillseven/LXX-Swete` | Strong's (`G1–G13149`), Robinson morph codes, lemmas, Swete verse numbers |
| **Packard's & Robinson's Morph Codes** | `Packard_s_and_Robinson_s_Morphological_Analysis_Codes_dct_<date>.dct.twm` | RMAC (Robinson) + PMAD (Packard/CATSS) | 6,102 morphology definitions covering 100% of canonical & deuterocanonical LXX tags |

See `LXX_Brenton_README.md` for detailed technical documentation on tagging, hover rules, and Brenton text repairs, and `change-logs/` for verse-level fix logs.

## Installation

1. Download the newest dated `.ot` and `.dct.twm` files from Releases (or `modules/`).
2. Place them in your theWord `Modules` folder alongside **`GBL-EPV`** (`SalitaNgDiyos/The-Greek-Bible-English-Lexicons`, module ID `jb51`).
3. Restart theWord.

## Sources, Credits & Licenses

- **Brenton Greek Text:** Sir Lancelot C. L. Brenton, *The Septuagint Version of the Old Testament* (1851/1879, public domain); foundational tagged theWord module by **Steve (`mathetes`)** on theWord forum; Brenton verse numbers and historical account from **communitychaplainfellowship.org**.
- **Rahlfs / CATSS Morphology (`LXX Rahlfs+` & `lxxmorph-rc.zip`):** CATSS LXX Morphology (Center for Computer Analysis of Texts, University of Pennsylvania, R. Kraft / E. Tov — **non-commercial CCAT user agreement**); `lxxmorph-rc` module by **Rúbio Terra**; 249 missing verses filled from **`eliranwong/LXX-Rahlfs-1935`** (**CC BY-NC-SA 4.0** / CCAT non-commercial).
- **Swete Greek Text (`SweteLXX+`):** H. B. Swete (1909–1930, public domain); digital text from **`eliranwong/LXX-Swete-1930`** (**GPL-3.0**, text supplied by Pasquale Amicarelli) and **`sleeptillseven/LXX-Swete`** (**CC BY-NC-SA 4.0**, non-commercial, First1KGreek-based); KJV versification mapping from **STEPBible TVTMS** (Tyndale House, **CC BY 4.0**).
- **Morphology Codes (`RMAC/PMAD`):** **Dr. Maurice A. Robinson** (RMAC), **David W. Packard / CATSS** (PMAD, non-commercial), **Costas Stergiou** (`theWord`), **Rúbio Terra**, and 2026 LXX/Deuterocanon extensions by **Edmund Paulino Valdez**.
- **Strong's Numbering & Companion Lexicon:** Aligned with **The Greek Bible English Lexicons (`GBL-EPV`)** (Strong's/Thayer, LSJ via Perseus Digital Library CC BY-SA 3.0 US, BDB).
- **Build & Audit Scripts (`tools/`):** Original scripts by Edmund Paulino Valdez licensed under **`AGPL-3.0-or-later`** (see `LICENSE`).
