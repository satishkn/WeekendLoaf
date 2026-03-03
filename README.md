# WeekendLoaf

This repository contains a simple **static website** for the WeekendLoaf bakery. The original site was a single HTML file exported from a live page; it's been refactored into a modular structure for easier editing.

## Structure

- `index.html` – home page.
- `pages/` – additional content pages (`about.html`, `products.html`, `contact.html`).

## Previewing the site

This project uses **absolute paths** (e.g. `/pages/about.html`, `/css/style.css`) so it must be served over HTTP. Open the root directory in a simple server, for example:

```bash
cd WeekendLoaf
python3 -m http.server 8000
```

Then visit `http://localhost:8000/` in your browser. Directly opening `index.html` with `file://` will break the navigation and partials because the leading slash points at your filesystem root.
- `css/style.css` – extracted stylesheet (original Tailwind utility-based styles).
- `partials/header.html` & `partials/footer.html` – shared header and footer markup loaded via JavaScript.
- `images/` – all graphic assets (logos, hero image, product photos, WhatsApp icon).
- `scripts/split_site.py` – helper script used to regenerate pages from a single-file source.

> **Note:** pages load the header/footer with `fetch()` at runtime, so ensure the files remain in their relative paths.

## Editing

1. Modify the content in `pages/` or `index.html` directly to change text or layout.
2. Update styles in `css/style.css` (or add new classes) as needed.
3. Add/replace images in `images/` and reference them via their filenames.
4. After making structural changes to the header or footer, update the corresponding partial and all HTML pages will reflect the change automatically.

To revert to the original single-file state, you can inspect `index_extracted.html` which preserves the full HTML snapshot.

---

Feel free to commit changes and deploy the static site to any simple host (GitHub Pages, Netlify, etc.).
