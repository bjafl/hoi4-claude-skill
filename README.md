# hoi4-claude-skill

A Claude Code / claude.ai skill that answers Hearts of Iron IV gameplay
questions from a curated, version-tagged wiki corpus instead of the model's
(often stale) training data.

## Why

HOI4's numbers, focus trees, and doctrine systems change with every patch and
DLC. Answering from memory alone goes stale fast — this project scrapes the
official wiki once, distills it into a lean reference corpus, and packages
it as a skill so Claude looks things up instead of guessing.

## Layout

```
skill/                     the shipped Claude skill
  hoi4-companion/          SKILL.md + references/ (copied from wiki-crawler/corpus/)
  hoi4-companion.skill     packaged upload for claude.ai (1.8 MB)
  hoi4-companion-workspace/  eval sets + description-optimization logs used to tune triggering

wiki-crawler/              build pipeline that produces the corpus
  fetcher/                 Python/Playwright scraper (hoi_wiki_crawler) that pulls pages from
                           hoi4.paradoxwikis.com
  corpus/                  staging corpus: raw scrape → distilled, front-mattered markdown
                           (see corpus/README.md, corpus/LEDGER.md, corpus/INDEX.md)
```

The corpus in `wiki-crawler/corpus/` is the **build/staging** copy; the skill
under `skill/hoi4-companion/references/` is the **shipped** copy. Fix content
issues in the corpus and re-copy — don't hand-edit the shipped copy.

## Using the skill

- **Claude Code**: point it at `skill/hoi4-companion/` (contains `SKILL.md`)
  as a project or personal skill.
- **claude.ai**: upload `skill/hoi4-companion.skill` directly.

See `skill/hoi4-companion/SKILL.md` for the routing table, triggering
description, and reference-file conventions.

## Rebuilding the corpus

1. `wiki-crawler/fetcher/` scrapes wiki pages (Playwright-based; see its
   `pyproject.toml` for the `uv`-managed Python environment).
2. Raw pages are distilled into `wiki-crawler/corpus/<category>/` following
   the front-matter and formatting rules in `corpus/_tooling/STYLE.md`.
3. Finished categories are copied into
   `skill/hoi4-companion/references/<same category>/`.

Current corpus: 250 files, ~7 MB, game version 1.19 unless a file's front
matter says otherwise. See `wiki-crawler/corpus/LEDGER.md` for build history
and known data-quality caveats.

## Attribution

Content derived from the [Hearts of Iron IV Wiki](https://hoi4.paradoxwikis.com),
published under Creative Commons Attribution-ShareAlike (CC BY-SA 3.0). Game
data is factual; prose has been rewritten and condensed. Retain attribution
and the same license if you redistribute.

Hearts of Iron IV is a trademark of Paradox Interactive. This project is not
affiliated with or endorsed by Paradox.

## License

Code is MIT ([LICENSE](LICENSE)); the wiki-derived corpus and skill content
are CC BY-SA 3.0 ([LICENSE-CONTENT.md](LICENSE-CONTENT.md)).
