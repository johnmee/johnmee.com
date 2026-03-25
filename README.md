# johnmee.com

Personal website for John Mee at [www.johnmee.com](https://www.johnmee.com). A minimalist blog and portfolio publishing technical articles, book reviews, and professional information.

## Architecture

A static site built with [Hugo](https://gohugo.io), deployed automatically to GitHub Pages on every push to `master`.

```
johnhugo/
├── .github/workflows/hugo.yml  # CI/CD: builds and deploys to GitHub Pages
├── archetypes/
│   └── default.md              # Template for new content (hugo new)
├── assets/
│   └── css/main.css            # All site styles (light/dark theme, responsive)
├── content/
│   ├── posts/                  # Blog posts (date-ordered)
│   └── disclaimer.md           # Disclaimer page (custom URL)
├── layouts/
│   └── _default/
│       ├── baseof.html         # Base template: header, footer, theme toggle
│       ├── home.html           # Homepage: latest 5 posts
│       ├── single.html         # Individual post/page
│       └── list.html           # Section index pages
├── static/                     # Served as-is: images, documents, favicon
└── hugo.toml                   # Site config: baseURL, title, tagline
```

No external theme is used — all templates are custom and contained in `layouts/`.

## Requirements

- [Hugo](https://gohugo.io/installation/) (extended version recommended)

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

## Deployment

Pushing to `master` triggers the GitHub Actions workflow (`.github/workflows/hugo.yml`), which builds the site and deploys it to GitHub Pages automatically. No manual steps required.

---

## How to Add a Post

**1. Create the file**

```sh
hugo new posts/my-post-title.md
```

This generates `content/posts/my-post-title.md` with front matter pre-filled from the archetype. The title is derived from the filename.

**2. Edit the front matter and content**

```markdown
+++
date = '2026-03-24T00:00:00+00:00'
draft = true
title = 'My Post Title'
+++

Your content here in Markdown.
```

- Set `draft = false` (or remove the line) when ready to publish.
- `date` controls sort order on the homepage and post list.

**3. Preview locally**

```sh
hugo server -D   # -D shows drafts
```

**4. Publish**

Set `draft = false` in the front matter, commit, and push to `master`. The site deploys automatically.

---

## How to Modify Templates and Layouts

All templates live in `layouts/_default/`. Hugo uses Go's `html/template` package.

### Base Template — `baseof.html`

Every page inherits from this. It defines the outer HTML shell:

- **Header** — site title (links to homepage), dark mode toggle button
- **Main content block** — `{{ block "main" . }}` — overridden by each template below
- **Footer** — copyright year and disclaimer link
- **CSS** — loaded from `assets/css/main.css` via Hugo's asset pipeline (minified + fingerprinted)
- **Theme script** — inline JS that reads/writes `localStorage` to persist light/dark preference

To change the site-wide header, footer, or add scripts that appear on every page, edit `baseof.html`.

### Homepage — `home.html`

Overrides the `main` block. Displays the five most recent posts from the `posts` section with their date, title, and summary. To change the number of posts shown, update the `first` parameter:

```html
{{ range first 5 (where .Site.RegularPages "Section" "posts") }}
```

### Single Post/Page — `single.html`

Renders an individual piece of content. Displays publish date, estimated reading time, and the full content body. Applied to every post in `content/posts/` and any standalone page like `content/disclaimer.md`.

### List Page — `list.html`

Renders section index pages (e.g. `/posts/`). Lists all pages in the section sorted by date, newest first. Each entry shows the date and a link to the page.

### Styles — `assets/css/main.css`

The stylesheet uses CSS custom properties for theming:

```css
:root { --bg: #fff; --text: #222; --accent: #0057b8; }
[data-theme="dark"] { --bg: #111; --text: #ddd; --accent: #58a6ff; }
```

- Edit `:root` and `[data-theme="dark"]` to change the colour scheme.
- The layout is a single centred column, max-width 860px.
- No external CSS frameworks are active — `normalize.css` and `skeleton.css` in `static/` are not currently loaded.

### Site Configuration — `hugo.toml`

```toml
baseURL = 'https://www.johnmee.com/'
languageCode = 'en-au'
title = 'John'

[params]
  tagline = 'The daily frustrations of man'
```

- `title` appears in the browser tab and is referenced in templates as `{{ .Site.Title }}`.
- `params.tagline` is available in templates as `{{ .Site.Params.tagline }}`.
