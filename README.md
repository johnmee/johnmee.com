# johnmee.com

Personal website for John Mee at [www.johnmee.com](https://www.johnmee.com). A minimalist blog and portfolio publishing technical articles, book reviews, and professional information.

Day-to-day editing — new posts, template changes, styling — is done with [Claude Code](https://claude.com/claude-code). See `CLAUDE.md` for the stack, conventions, and gotchas it needs to know. This file just covers what a human (or a first Claude session) needs to get the site running.

## Architecture

A static site built with [Hugo](https://gohugo.io), deployed automatically to GitHub Pages on every push to `master`. No external theme — all templates are hand-written in `layouts/`.

```
johnhugo/
├── .github/workflows/hugo.yml  # CI/CD: builds and deploys to GitHub Pages
├── archetypes/
│   └── default.md              # Template for new content (hugo new)
├── assets/
│   ├── css/main.css            # All site styles (light/dark theme, responsive)
│   └── images/                 # Assets run through Hugo's image pipeline
├── content/
│   ├── posts/                  # Blog posts (date-ordered)
│   ├── contact.md              # Contact page and PGP public key
│   └── disclaimer.md           # Disclaimer page (custom URL)
├── layouts/
│   ├── baseof.html             # Base template: header, footer, theme toggle
│   ├── home.html               # Homepage: latest 5 posts
│   ├── list.html                # Section index pages
│   ├── single.html              # Individual post/page
│   ├── _markup/                 # Render hooks (images, tables)
│   ├── _partials/                # Shared partials (post-list-item)
│   └── _shortcodes/              # Shortcodes (bot-resistant email link)
├── static/                     # Served as-is: images, documents, favicon
├── .stylelintrc.json           # CSS lint rules
├── package.json                # stylelint, via `npm run lint:css`
└── hugo.toml                   # Site config: baseURL, title, tagline
```

## Content & Assets

A few files under `static/` are kept deliberately even though nothing on the site links to them — personal archive, not oversight:

- `images/resume/` — company logos from an older resume design.
- `images/oodnadata_track.jpeg` — background image from a retired stylesheet.
- `resume.docx` — an older resume with images worth keeping.

`static/css/normalize.css` and `skeleton.css` (unused CSS frameworks from an earlier iteration of the site) were removed — they conflicted with the current custom theming system and had nothing worth salvaging.

## Requirements

- [Hugo](https://gohugo.io/installation/) extended, **0.164 or newer** (the templates rely on the 0.146+ layout lookup system — see `CLAUDE.md`).
- [Node.js](https://nodejs.org/) + npm, for CSS linting only.

```sh
hugo version
```

## Local Development

```sh
git clone https://github.com/johnmee/johnhugo.git
cd johnhugo

# Start local dev server with drafts visible
hugo server -D

# Visit http://localhost:1313
```

## Linting

```sh
npm install
npm run lint:css
```

Lints `assets/css/main.css` with stylelint. Run it after any CSS change.

## Deployment

Pushing to `master` triggers the GitHub Actions workflow (`.github/workflows/hugo.yml`), which builds the site and deploys it to GitHub Pages automatically. No manual steps required.
