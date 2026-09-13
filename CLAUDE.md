# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Static product site for the Ohayo apps (`https://apps.ohayo.by`), deployed by Cloudflare Workers Assets on every push to `main`. No build step, no dependencies, no tests, no linter. [README.md](README.md) is the full reference; the essentials are below.

## Commands

```sh
python3 render.py                 # regenerate all pages, Markdown twins, llms.txt, sitemap.xml
python3 -m http.server 8899       # preview from the repo root (pages use absolute /assets/... paths)
swift tools/avif.swift assets/ohayo-network/{en,ru}/{popover,dashboard,per-app,settings}.png   # PNG -> AVIF
```

`render.py` fails loudly on any unfilled `{{PLACEHOLDER}}` — that is the only validation. `http.server` does not reproduce Cloudflare routing or `_headers`; for that run `npx wrangler dev` against a copy of the site **outside** the repo (in place, `.wrangler/` writes cause an endless reload loop).

## Architecture

- **The repo root is the deploy root** (`wrangler.jsonc` → `assets.directory: "."`). Every file is publicly served unless listed in `.assetsignore`. Any new non-site file (docs, tooling, configs — including `CLAUDE.md` and `.claude/`) must be added there. A `_redirects` 404 rule is not an alternative: it fails the whole deploy.
- **Generated vs. source.** `index.html`, `ru/index.html`, `ohayo-network/index.html`, `ohayo-network/ru/index.html`, `ohayo-network.md`, `ohayo-network/ru.md`, `llms.txt`, `sitemap.xml` are generated — never hand-edit them. Structure lives in `templates/*.tmpl.html`; copy for both locales (`en`, `ru`) lives in `STRINGS` in `render.py`; output paths in `LOCALES`; page types in `PAGES`. JSON-LD (`@graph`) and the Markdown twins are built in `render.py` from the same `STRINGS`, so copy changes propagate everywhere. `404.html` and `robots.txt` are hand-maintained.
- **Asset cache busting.** `/assets/*` is served `immutable` for a year; `render.py` stamps every `/assets/...` reference with `?v=<sha256 prefix>`. **Any change to `assets/site.css`, `site.js`, images, etc. requires re-running `render.py`**, otherwise browsers keep the old file.
- **Sitemap `lastmod`** = date of the last commit touching the page, or today if the page file is uncommitted/dirty.
- **i18n.** English is canonical (`/ohayo-network`), Russian at `/ohayo-network/ru`, linked via `hreflang` + `x-default`. No locale redirects by design; `assets/site.js` shows a dismissible Russian hint on English pages (`localStorage` key `ohayo.lang`).
- **JS is progressive enhancement only** (`assets/head.js` adds the `.js` class pre-paint; `assets/site.js` handles sticky header state, lang hint, reveals). Pages must be complete without it.
- **CSS** is a single `assets/site.css`; mobile breakpoints are `900px` and `620px`. Decorative glow halos use negative-inset `::before`; `main { overflow-x: clip }` stops them widening the mobile layout viewport.

## Constraints

- **Zero third-party requests**: no web fonts, analytics, CDNs. The CSP in `_headers` (`default-src 'self'`, no inline scripts) enforces it.
- **URLs are published** (App Store Connect Marketing URL) — never break or rename one. Keep `html_handling: "drop-trailing-slash"`; the default would 307 every canonical URL.
- **JSON-LD carries no price and no version** — the Mac App Store owns both.
- Apple Mac App Store badges (`assets/badge-mas-*.svg`) are official artwork: never recolour/crop/rebuild, match locale to page.
- `assets/ohayo-network/icon.svg` is the app icon — only on that app's pages/card. The studio mark is `assets/mark.svg` (hub, 404).
- Screenshots come from the Ohayo Network repo (`dist/screenshots/raw/<locale>/`) with personal data already pixelated; re-shoot there, copy here, regenerate AVIF, re-run `render.py`.
- Legal/support pages live in the sibling `ohayo-legal` repo (`legal.ohayo.by/network/{support,privacy,eula}`); keep links in step.

## Git

- Commit messages: short, one line.
- No `Co-Authored-By` or any other attribution trailers.
- Commit directly to `main`; create a branch only when the user explicitly asks for one. Pushing `main` deploys to production.

## Adding an app

Card in `templates/home.tmpl.html` + copy in `STRINGS` (both locales), new `templates/<slug>.tmpl.html`, entry in `PAGES` and output paths in `LOCALES`, screenshots in `assets/<slug>/<locale>/`, extend `.assetsignore`/`_headers` if new Markdown twins are added, then `python3 render.py`.
