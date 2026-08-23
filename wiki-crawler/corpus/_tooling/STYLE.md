# Knowledge-base authoring rules (all writers follow these)

The audience is **an LLM agent** that will be asked things like "I'm playing Romania in 1937, what
should I do?", "how does supply work?", "how do I get the Cheese your fighter achievement?". Docs
must be dense, scannable, and factual. No fluff, no marketing, no "this wiki is community
maintained" boilerplate.

## Language
English. All game terms exactly as they appear in-game (focus names, national spirit names,
country tags, technology names).

## Every file starts with YAML front matter

```yaml
---
title: Supply and Logistics
category: mechanics
tags: [supply, logistics, railways, trucks, ports, attrition]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Logistics
---
```

- `dlc:` lists DLC required for the content described (`[]` if base game).
- `game_version:` — take from the wiki page's version banner if present, else `"1.19"`.
- `sources:` — every wiki page URL you drew on. Required.

Follow the front matter with a 2–4 sentence **Summary** section, then the body.

## Body rules

1. **Keep the numbers.** Stat tables, modifier values, costs, requirements, formulas — reproduce
   these as markdown tables. They are the whole point. Never round, never "approximately".
2. **Rewrite the prose.** Do not paste wiki paragraphs. Compress explanation into your own tight
   sentences and bullets. Aim for roughly half the wiki's word count on prose while keeping 100%
   of the data.
3. **Strip icon noise.** The extractor leaves markers like `[Flag of Germany]`, `[Attack.png]`,
   `[Political power]`. Delete them, or fold them into the term (`[Political power]political power`
   → `political power`). Never leave bare `.png` text in a table cell.
4. **Delete navigation cruft.** The tail of every page has "Warfare / Land warfare / Naval
   warfare ..." navbox tables — drop them. Also drop "External guides", "References" link lists,
   and edit links.
5. **Mark DLC gating inline** whenever a mechanic, focus branch, or unit requires DLC:
   `(requires No Step Back)`.
6. **Flag uncertainty.** If the wiki is self-contradictory, outdated, or the page carries an
   "outdated" banner, add `> ⚠️ Wiki flags this section as potentially outdated (last verified
   patch X).`
7. **Cross-link** with relative paths: `See [Division designer](../02-land-warfare/division-designer.md)`.
8. **Do not invent.** If you don't have the data, write `_Not covered on the wiki._` rather than
   guessing. Strategy advice you infer must be labelled `**Inferred:**`.
9. Headings: file starts at `##` (the `title:` in front matter is the H1). Never emit `#`.
10. Long files are fine — 3000+ lines is acceptable for focus trees. Do not truncate to save space.

## File naming
`lowercase-with-hyphens.md`. Country files use the common English name: `germany.md`,
`soviet-union.md`, `united-kingdom.md`, `nationalist-spain.md`.

## When you finish
Append one line per file you wrote to `_tooling/manifest.tsv` (path relative to the
`wiki-crawler/corpus/` knowledge-base root — do not hardcode an absolute path, it will
differ per environment/session):

```
printf '%s\t%s\t%s\t%s\n' "<relpath>" "<title>" "<bytes>" "<comma,separated,source,pages>" >> _tooling/manifest.tsv
```

(Use `>>` — many agents append concurrently. One `printf` per file, never rewrite the file.)
