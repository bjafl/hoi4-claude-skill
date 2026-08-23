# Reference Data Format

This directory is a **build output**, not where content is authored. Content
is fetched and written in `wiki-crawler/corpus/` at the repo root —
see that directory's `_tooling/STYLE.md` for the authoring rules (front
matter schema, table/number-fidelity rules, condensing rules) and
`LEDGER.md` for build progress. Once a category there is complete and any
condensing decisions from `SKILL.md`'s "Keep reference files lean" section
have been applied, the finished files are copied here unchanged.

Do not hand-edit files in this directory to fix content issues — fix them
in the source category under `wiki-crawler/corpus/` and re-copy, or
the fix will be lost the next time that category is refreshed.

## Naming convention

Directory names mirror `wiki-crawler/corpus/`'s categories exactly
(`00-meta/`, `01-mechanics/`, `02-land-warfare/`, `03-air-warfare/`,
`04-naval-warfare/`, `05-countries/`, `06-focus-trees/`, `07-achievements/`,
`08-strategy/`, `09-reference/`) so files can be synced across without
renaming. See `SKILL.md`'s reference table for what belongs in each.

## One file per topic

Keep files scoped to one topic/country/category so Claude only loads what's
relevant to a question instead of pulling in the whole corpus every time —
the same reason `SKILL.md` itself stays a short index rather than
containing all the data directly.
