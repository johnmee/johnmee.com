# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal blog and portfolio of a software developer based in Sydney, Australia, published at johnmee.com. Posts cover technical topics, book/product reviews, and professional info (resume). Tone is informal (`tagline = 'The daily frustrations of man'`).

## Stack

- Hugo extended, **>= 0.164** (pin to this or newer — the site relies on 0.146+ template lookup behaviour, see below).
- No CSS framework. All styling is hand-written in `assets/css/main.css` using CSS custom properties for light/dark theming (`[data-theme]`). `normalize.css` and `skeleton.css` sit unused in `static/css/` — leftover, not wired into any template.
- No JavaScript framework. The only client-side JS is two inline `<script>` blocks in `layouts/baseof.html`: one resolves the theme before first paint, the other wires the toggle button. Keep it that way unless asked otherwise.
- No theme — all templates are hand-written under `layouts/`.

## Hugo template layout paths

This repo uses the modern (0.146+) layout system, not the legacy one. Hugo 0.164 does **not** warn on legacy paths, so mistakes here fail silently instead of erroring:

- Page templates (`baseof.html`, `home.html`, `list.html`, `single.html`) live directly under `layouts/` — not `layouts/_default/`.
- Render hooks go in `layouts/_markup/` (e.g. `render-image.html`, `render-table.html`) — not `layouts/_default/_markup/`.
- Partials go in `layouts/_partials/` — not `layouts/partials/`.
- Shortcodes, if added, go in `layouts/_shortcodes/`.

## Content frontmatter

Posts use YAML (`---`) frontmatter with `title`, `date`, `tagline`, `tags`, `categories`, `draft`. `archetypes/default.md` defaults to TOML (`+++`) — if scaffolding a post with `hugo new`, convert the frontmatter to YAML to match every existing post.

## Build

- `hugo server -D` for local dev with drafts visible.
- `hugo --destination public` currently builds with **zero warnings** — treat any new warning as a bug to fix, not something to ignore.
- `npm install` then `npm run lint:css` lints `assets/css/main.css` with stylelint (`stylelint-config-standard`, `no-descending-specificity` disabled — see `.stylelintrc.json`). Run after any CSS edit.
- CI (`.github/workflows/hugo.yml`) builds and deploys to GitHub Pages on every push to `master`. No manual deploy step.

## Gotchas

- `resources.Get "x" | images.Resize ...` is not valid on this Hugo version — `Resize` isn't a pipeline function. Use the method form: `(resources.Get "images/x.png").Resize "200x webp q90"`.
- `static/meejinnz/index.html` and `static/resume-2026.html` are intentionally hand-written outside the Hugo template system — the former is a deliberate 1999-style period piece (nested tables, `bgcolor`). Don't "fix" or modernize either.
- `public/` and `resources/` are build output/image cache (gitignored) — never hand-edit.

See `JOURNAL.md` in this directory for a log of past session work.
