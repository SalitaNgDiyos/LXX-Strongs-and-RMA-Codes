# LXX Brenton+ (TheWord Bible module)

## For readers

**LXX Brenton+** is the Greek Old Testament (the Septuagint) for the free [TheWord](https://www.theword.net) Bible program, based on Sir Lancelot C. L. Brenton's edition. **Every Greek word is now tagged.** Each one carries:

- a **Strong's number**, which opens that word's dictionary entry when you hover over or click it, and
- a **grammar code**, which tells you the word's form (tense, voice, mood, case, number, person).

### What this release adds

- **Complete coverage.** All 23,145 verses, about 479,000 words, are tagged. Earlier versions had thousands of untagged words and placeholder grammar codes.
- **Standard Strong's numbers wherever possible.** If a Septuagint word is the same word that appears in the New Testament, it uses the familiar Strong's/Thayer number, even when the spelling or form differs. A Strong's search can therefore follow a word from the Old Testament into the New.
- **New numbers for Septuagint-only words.** Words and names that never appear in the New Testament use new numbers **G6135–G12916**: about 3,100 names of people and places and about 3,750 other words.
- **Compound numbers tagged by their parts.** For example, τεσσαρακονταπέντε ("forty-five") is tagged 40 + 5, so it turns up in a search for either number.
- **Corrected grammar codes.** Placeholder and wrong codes were replaced with proper parsings.
- **Brenton verse numbers.** Each verse shows Brenton's own verse number in blue (press "v" to show or hide), useful where the Septuagint and KJV numbering differ.
- **Pop-up word details.** Hover over any Greek word to see its Strong's number, dictionary entry and grammar code in a pop-up, even when the Strong's numbers and grammar codes are hidden in the text.
- **A few repaired words.** Six words that had been broken apart or run together in the printed Greek were restored to the standard Septuagint reading.

### Installation

1. Copy `LXX Brenton+.ot` into your TheWord modules folder.
2. Also install the companion dictionary, **EPV Greek Definitions** (`epv-thayer-kjv_dct.twm`). It has an entry for every Strong's number used in this module.
3. Restart TheWord.

---

## For module developers

### File

| Property | Value |
|---|---|
| Format | TheWord OT Bible module (`.ot`) |
| Encoding | UTF-8 **with BOM**, CRLF line endings |
| Lines | 23,145 (one verse per line). Aligns line-for-line with `lxxmorph-rc.ot` and the KJV module `akjvpce.ont` |
| Text | Brenton Greek, unchanged apart from the six repairs listed below; all other changes are tags only |

### Tag format

```
πρὸς<WG4314><WTPREP> τὸν<WG3588><WTT-ASM> Θεὸν<WG2316><WTN-ASM>
```

- **479,787** `<WG>` Strong's tags and **479,354** `<WT>` morph tags. A few original multi-code tokens keep two `<WT>` tags.
- Every Greek word has a `<WG>` tag, and every `<WT>` tag has a `<WG>` before it.
- **10,775** distinct Strong's numbers are used.

### Strong's numbering

| Range | Source | Distinct numbers in module |
|---|---|---|
| G1–G5624 | Strong's / Thayer | 3,495 |
| G5625–G6134 | Existing EPV extensions (e.g. G5626 ἐνενήκοντα) | 498 |
| G6135–G12916 | New LXX-only entries, continuous with no gaps | 6,782 |

The selection rules, applied in order:

1. **Existing numbers come first.** A word takes a Thayer number whenever its lemma matches, including Thayer/LXX spelling variants: ἐξολεθρεύω/ἐξολοθρεύω, ῤῥ/ρρ, ῳ/ω, σσ/ττ, and active/deponent pairs.
2. **Proper nouns** take a number only from the EPV dictionary; otherwise they get a new one.
3. **One number per lemma.** Inflected forms share a single number.

### Multiple `<WG>` tags (compound numerals)

The word's own number comes first, followed by the numbers of its parts. Words that already had a number for the whole number were left unchanged.

```
τεσσαρακονταπέντε<WG5062><WG4002>              40 + 5 (no Strong's number exists for 45)
ἑβδομηκονταδύο<WG10581><WG1440><WG1417>        own entry, then 70 + 2
ὀκτωκαιδέκατος<WG9208><WG3638><WG1182>         ordinal: unit + δέκατος
δεκατέσσαρα<WG6135><WG1180>                    Thayer's whole-number equivalent added
```

230 tokens are affected. Ninety has no Strong's number, so EPV G5626 serves as the tens component.

### Morphology

- Codes are Packard's, with Robinson's as fallback (e.g. `VAI-AAI3S`, `V-AAI-3S`, `N2-GSM`, `A1-NSMS`, `N-PRI`). All of them resolve in *Packard's and Robinson's Morphological Analysis Codes*.
- Sources, in order of preference:
  1. `lxxmorph-rc`
  2. the audited `Suggested_Code`
  3. hand parsing
- Every `<WTA-->` placeholder has been replaced.

### Verse rule (hover pop-ups)

The properties section after the last verse holds one `verse.rule`, modelled on the one in Byz2005+:

```
verse.rule="([^\s<>{}()\[\],.;:]+)(<W(G\d+)>)(<W(G\d+)>)?(<W(G\d+)>)?(<W(G\d+)>)?(<WT([^>]+)>)?(<WT([^>]+)>)?" "<a href=""_ORIGWORD_$1|_STRONG_$3|_STRONG2_$5|_STRONG3_$7|_STRONG4_$9|_MORPH_$11|_MORPH2_$13|_NOLINK_"">$1</a>$2$4$6$8$10$12"
```

- It turns every tagged word into a link that carries the word, up to four Strong's numbers (compound numerals) and up to two morph codes. Hovering over the word shows them in TheWord's pop-up.
- The original `<WG>`/`<WT>` tags are written back after the link, so TheWord's Strong's and morphology display toggles still work.
- Unlike Byz2005+, the module has no `<wt>` marker or `l="lemma"` attribute. The word is matched as the run of characters before the first `<WG>` tag, excluding whitespace, tags and ASCII punctuation, and the lemma comes from the dictionary entry the Strong's number opens.
- Tested against every verse: all 479,355 tagged words become links, and stripping the links gives back the verse unchanged.

### Brenton verse numbers

Every verse line now begins with Brenton's own verse number in a `<Q n<q>` tag (23,124 tags, taken from *The Septuagint Version - Greek* module by communitychaplainfellowship.org). Where Brenton's numbering differs, both are given, e.g. `<Q 15(13) <q>`; 65 tags fall inside a line where a Brenton verse starts mid-verse. A second verse rule shows them in small blue type, toggled with the "v" key:

```
verse.rule="<Q (.*?)<q>" "<NB toggle=v><font color=blue size=-1>$1</font><Nb>"
```

These replace the 232 malformed `<Q` tags in the earlier file. No words or tags were changed.

### Module properties

After the verse rule the file has the standard properties: `lang=grc`, `short.title=LXX Brenton+`, `description`, `version.major=1`, `version.minor=0`, `version.date=2026-10-16`, `creator` and an HTML `about` text, which includes Brenton's "An Historical Account of the Septuagint Version" (1879).

### Duplicate cleanup (October 2026)

- 95 duplicate new entries were merged: 45 into the existing EPV entry for the same word (e.g. Μωαβίτης G7507 → EPV G5867) and 50 into another new entry that differed only in accent, capitals or spelling.
- Tokens that sat on the wrong existing entry were moved, e.g. ῥομφαία from EPV G5653 to Thayer G4501, and πονηρεύομαι from G4189 πονηρία to EPV G5858.
- The freed numbers were filled by moving the highest numbers down, so G6135–G12916 is still continuous. The maps are in `duplicate_entries_merged_report.csv` and `gap_fill_renumbering.csv`. Older reports show the numbers as they were before this cleanup.

### Text corrections against the printed Brenton (October 2026)

The Greek text was compared with a scan of Brenton's printed edition (*The Septuagint Version of the Old Testament and Apocrypha*). 590 words were corrected to the printed form: 278 spelling errors (e.g. ὅραι → ὅρια, γστρὶ → γαστρὶ) and 312 accent or breathing errors (e.g. τὼν → τῶν, πᾶσῃ → πάσῃ). Each correction was confirmed by a second OCR reading or checked against the page image; Strong's numbers and morph codes were kept. Malachi 4:6, which contained the text of Genesis 22:16, now has Brenton's verse "Μνήσθητε νόμου Μωυσῆ…" and was re-tagged. 37 dictionary entries that had been created for misspelt forms were merged into the entry for the real word, and 11 were renamed to their dictionary form. The full list is in `brenton_text_corrections.csv`; the comparison is in `brenton_text_check_report.csv`.

Still differing from Brenton (left for review): about 1,500 readings where the module has another word or form (often the Rahlfs reading), and about 60 verses that Brenton does not print (e.g. 1 Sam 17:12–31, 1 Kgs 6:11–13, 1 Chr 1:11–23).

### Text repairs

Made only where a word was broken or merged, following the standard LXX text:

- Θε + õν → Θεὸν (Exod 18:19)
- Ἐλι + àφ → Ἐλιάφ (1 Kgs 4:3)
- ἀπὸλύων → ἀπὸ ὀλίγων (Ps 17:14)
- οἶσα → εὐλαβηθεῖσα (Isa 51:12)
- Βαθησὰ + ρ → Βαθησὰρ (Josh 15:44)
- ἩΣΑΪ + ́ΑΣ → ἩΣΑΪ́ΑΣ (Isa 13:1); the tags had been inserted inside the word

Other misprints are left as printed but tagged with the intended lemma (e.g. ἀμενεῖ → G1696 ἐμμένω).

### Supporting reports (CSV, UTF-8 with BOM)

| File | Contents |
|---|---|
| `new_strongs_numbers_report.csv` | Every token that received a number |
| `existing_strongs_remap_report.csv` | Provisional numbers replaced by Thayer numbers |
| `merged_duplicate_entries_report.csv` | Lemma groups merged into one number |
| `strongs_renumbering_map.csv` | Old number → current number |
| `duplicate_entries_merged_report.csv`, `gap_fill_renumbering.csv` | Duplicate-entry merges and the renumbering that closed the gaps |
| `numeral_components_report.csv` | Compound-numeral tags before and after |
| `orphan_words_tagged.csv`, `strongs_leftover_words_tagged.csv` | The last untagged words and how they were resolved |
| `morph_*` reports | Morphology fixes and additions |

`missing_strongs_new_numbers.csv` is an obsolete draft with superseded numbering. Do not use it.

### Acknowledgements

- Brenton's Septuagint (Greek text).
- The LXX morphological database; Packard's and Robinson's morphological codes.
- Strong's / Thayer numbering.
- The KJV with Strong's numbers, used for alignment.
