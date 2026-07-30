# Prompt: foundational fixes for johnhugo (pre-styling)

Copy everything below the line into a new session.

---

I have a Hugo blog at `/home/john/code/johnmee/johnhugo` (Hugo **0.164.0 extended**, no theme, hand-written templates in `layouts/`, one stylesheet at `assets/css/main.css`). The design is deliberately minimalistic. I think it currently reads bland and unpolished, but **do not touch CSS, typography, colour, spacing, or layout yet.**

A previous attempt jumped to a full visual redesign — self-hosted Source Serif 4 + Public Sans, a warm "paper on a desk" frame, a 52rem sheet with a 36rem measure, a token system and two breakpoints. **I rejected it.** Do not reproduce that direction. Treat the visual direction as an open question we have not settled.

What I want from you first is the **non-cosmetic, foundational layer**: correctness, semantics, template bugs, and missing behaviour. Work through the list below. Everything in it was verified empirically against this repo, with file:line references — but re-verify before acting, since I have reverted the working tree since it was written.

## Ground rules

- **Never run `git commit` or `git add`.** All commits are mine (this is in my global CLAUDE.md). Read-only git is fine. Leave work in the working tree and tell me it's ready.
- **Never use blanket `git checkout .`, `git reset --hard`, or `git clean`.** A previous session destroyed an uncommitted edit of mine that way. Test experiments in a copy, or reverse a specific change with a targeted command.
- Prefer `fdfind` / `rg` / the `Glob` tool over `find`. There is no `fd` binary on this system. Use the `Edit` tool for in-place edits, not `sed -i`.
- `hugo` currently builds with exactly one warning (item 2). Once that's fixed, treat "zero warnings" as a gate.

## A. Build & config correctness

1. **Migrate to the Hugo 0.146+ template system.** `layouts/_default/_markup/render-table.html` is on the legacy path. Hugo 0.164 emits **no deprecation warning** for legacy layout paths, so the build will never flag it. Move it to `layouts/_markup/`. Anything new goes in `layouts/_partials/` and `layouts/_shortcodes/` — never `layouts/partials/` or `layouts/_default/`. My four page templates (`baseof`, `home`, `list`, `single`) are already correctly at `layouts/` root. Verify tables still render afterwards.

2. **`hugo.toml`: `languageCode` → `locale`.** Deprecated in Hugo 0.158.0. This is currently the only build warning.

3. **Add `resources/` to `.gitignore`** before using Hugo's image pipeline. There may already be an untracked `resources/` directory present — it is orphaned scratch and safe to delete.

## B. Semantics & markup structure

4. **Five posts emit a second `<h1>`.** `single.html` outputs the page title as `<h1>`, and these posts also use `#` in the body: `linux-nvidia-8700.md` (9), `book-list.md` (5), `suffering.md` (3), `minimum-wage.md` (1), `travel-letters-indonesia-hawaii-usa-canada.md` (1).
   - **This cannot be a `render-heading.html` hook.** A blanket h1→h2 demote collapses a level in `suffering.md` (which has `# Discussion` followed by `## Suicide?`) and in `travel-letters` (three genuine levels). Each file needs its own shift. Do the deepest level first so edits can't collide.
   - Two files have bugs beyond the extra h1: `minimum-wage.md` jumps `#` → `###` with no h2 at all; `travel-letters` has `## October 20, 1992` at place-level sitting directly under `### October 19, 1992`. In travel-letters the intended structure is places at `##`, dates at `###`.
   - **Trap:** `rg '^# ' content/posts/` overcounts — it matches `#` comments inside fenced code blocks. That error previously produced a wrong count of seven files. `how-this-website-works.md` and `how-to-send-secure-email-with-the-gmail-api.md` are already correct; their hits are Python comments. Enumerate headings with a fence-aware script.
   - Success condition: `rg -c '<h1' public/posts/*/index.html` returns `:1` on every line (read every line — it prints counts and won't fail loudly on a `2`).

5. **Every image renders as `<p><img>`.** Goldmark wraps them, so any `> img` CSS selector silently matches nothing. Counts: `travel-letters` 27, `how-to-be-a-frontend-developer` 6, `chair-review-aeron-vs-leap` 2, plus singles in `my-au-pairit-reality` and `a-technical-interview`.
   - `wrapStandAloneImageWithinParagraph = false` in `hugo.toml` unwraps **single** images only.
   - **Consecutive image lines form one paragraph**, which that setting does not unwrap. About 8 image *groups* stay as `<p><img><img></p>`. This is my actual authoring convention in `travel-letters` (2–3 photos stacked with no blank line between), so it needs a deliberate decision rather than just the config flag.
   - A `layouts/_markup/render-image.html` hook is the right tool. Verified working on 0.164: both `.IsBlock` (distinguishes block from inline) and `.PlainText` (alt text) are available.
   - Also verified: **no paragraph anywhere on this site mixes an image with text**, so treating any image-bearing paragraph as a block is safe. Re-confirm before relying on it.

6. **No image anywhere has `loading="lazy"`.** `travel-letters` loads 39 images eagerly.

7. **`home.html` and `list.html` duplicate the post-list markup**, and `home.html` hardcodes a `<li>` for the `/meejinnz/` page. Factor into a shared partial. It must take a **dict**, not a `Page` — meejinnz is hand-written HTML in `static/` with no front matter to read.

## C. Live template bugs

8. **`single.html` renders a dangling separator today.** The meta guard is an `or`, so `/disclaimer` — which has a reading time but no date — currently outputs a leading ` · `:
   ```html
   <div class="post-meta">
        &nbsp;·&nbsp;
       1 min read
   </div>
   ```
   Build the parts into a slice and `delimit` them.

9. **The theme toggle is broken four ways**, all behavioural:
   - The theme is set **twice** — once in the `<head>` script and again at end of `<body>` — and the end-of-body copy hardcodes `|| 'light'`, so it **clobbers whatever the head decided** on every page load. Adding `prefers-color-scheme` to the head alone will do nothing.
   - `prefers-color-scheme` is ignored entirely; users with dark OS settings get a light page.
   - `<html ... data-theme="light">` is hardcoded, which is a lie in dark mode.
   - The button hardcodes `☀︎` in markup while the default theme is light, so the wrong glyph paints before JS runs.

   Resolve the theme in exactly one place (the head, before first paint) and let the end-of-body script do wiring only. Consider driving the glyph from CSS off `[data-theme]` so it needs no JS timing at all.

10. **The logo is a 1024×1024 PNG served at 100px** — a 10× browser downscale on every page load. It needs to move to `assets/` to use Hugo's image pipeline. Its `alt="John logo"` also duplicates the adjacent site title and should be `alt=""`.

## D. Missing behaviour

11. **The `<head>` contains three tags total**: `viewport`, `stylesheet`, `icon`. No description, no canonical, no Open Graph. This matters beyond SEO because `single.html` puts a **Share button on every post** — shared links currently paste into Slack/iMessage/Signal as bare URLs with no title, description, or image. The copy already exists: every rendered post has a `tagline` in front matter. (`content/posts/resume.md` is `draft: true`, so the site-tagline fallback is only exercised by `/disclaimer`.) An `og:image` needs a **stable, unfingerprinted** URL — see the gotcha below about which logo files actually exist.

12. **No `:focus-visible` rule anywhere**, on buttons that are `background: none` — keyboard users get no visible focus indicator at all. And **`prefers-reduced-motion` is not respected** despite a `transition` on `body`. Both are behaviour, not decoration.

13. **Tap targets are ~26–30px** (`#theme-toggle`, `.share-btn`, `.post-tags a`) against a 44px minimum. Fixing this forces `.post-tags` into a wrapping flex row, so it is a structural change rather than a padding tweak.

## Explicitly out of scope — do not modify

- `static/meejinnz/index.html` — 35KB of 1999-vintage HTML 4.0 Transitional, nested `<table width="80%">`, `bgcolor`, Verdana. A deliberate period artifact; its jank is the point. It already has a viewport meta.
- `static/resume-2026.html` — hand-written, outside the layout system, already has its own viewport meta and media queries.
- `static/google-evaluation.html`.

## Gotchas verified the hard way — don't rediscover these

- **`images.Resize` does not exist as a pipeline function on 0.164.** `resources.Get "x" | images.Resize "96x"` fails with `can't evaluate field Resize in type interface {}`. Use the method form: `(resources.Get "images/x.png").Resize "96x webp q90"`.
- **Headless Chromium reports `prefers-color-scheme: dark` by default.** For light screenshots pass `--blink-settings=preferredColorScheme=1`; omit it for dark. `--force-dark-mode` does **not** control the media query, and `preferredColorScheme=2` does not produce dark either. Chromium is at `/usr/bin/chromium`; PIL 12.2 is available for pixel assertions on screenshots.
- **`snoopy_logo_alt.png` and `snoopy_logo_blog.png` exist only in `public/`** — stale build output from an older revision, not source. `static/` contains only `snoopy_logo.png`. Anything referencing the other two will 404.
- **A headless window much taller than the page tiles the render**, producing a convincing fake "duplicate header" in the screenshot. Not a template bug — size the window to the content, and check the DOM before believing a visual anomaly.
- **Three characters in my content fall outside the Google/Fontsource "latin" subset**, if webfonts ever come up: `→` (U+2192), `≠` (U+2260), `⚠` (U+26A0), 5 uses total. They fall back through the font stack rather than showing tofu, and `latin-ext` would **not** fix them — they are arrows and symbols, not Latin letters.
- `.superpowers/sdd/2026-07-30-blog-polish-mobile/` holds a ledger and per-task rollback patches from the rejected attempt. Ignore it or delete it; it is git-ignored scratch.

## How to proceed

1. Re-verify the items above against the current tree before changing anything — the tree has been reverted since these were recorded.
2. Tell me if any item is wrong or no longer applies.
3. Work through A → D. Keep `hugo` at zero warnings throughout, and verify each change against rendered output in `public/` rather than asserting it.
4. **Stop before any CSS/styling work** and check in.

Finally: ask me what specifically I disliked about the rejected redesign before you propose any visual direction. Whether it was the typeface pairing, the paper-on-desk frame, or simply that the whole thing felt over-designed changes what should happen next — and I'd rather tell you than have you guess.
