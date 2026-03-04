# Weekend Loaf

A Jekyll-based website for **Weekend Loaf**, a small-batch artisan masala bread bakery in Austin, Texas. Hand-crafted loaves with bold spices, fresh ingredients, and weekend traditions.

## Site Structure

```
├── index.html           # Home page (displays latest bread posts)
├── about.html           # About Weekend Loaf story
├── contact.html         # Contact & ordering information
├── products.html         # Browse all breads & products
├── _posts/              # Bread & product posts (Markdown files)
├── _layouts/            # Page templates
├── _includes/           # Reusable components
├── _config.yml          # Site configuration
├── css/                 # Stylesheets
└── images/              # Logo, product photos, hero image
```

## Previewing the site

This project uses **absolute paths** (e.g. `/pages/about.html`, `/css/style.css`) so it must be served over HTTP. Open the root directory in a simple server, for example:

```bash
cd WeekendLoaf
python3 -m http.server 8000
```

Then visit `http://localhost:4000/` in your browser; Jekyll will rebuild automatically as you edit.

- `css/` – stylesheets (Sass files compiled by Jekyll).
- `images/` – all graphic assets (logos, hero image, product photos, WhatsApp icon).
- `_posts/` – Markdown files representing each bread/product.
- `_layouts/` and `_includes/` contain the templates used by pages and posts.

> **Note:** because this is a Jekyll site, you don't need to worry about manually including headers/footers; they're injected via the layouts.

## Editing

1. Modify the content in `pages/` or `index.html` directly to change text or layout.
2. Update styles in `css/style.css` (or add new classes) as needed.
3. Add/replace images in `images/` and reference them via their filenames.
4. After making structural changes to the header or footer, update the corresponding partial and all HTML pages will reflect the change automatically.

To revert to the original single-file state, you can inspect `index_extracted.html` which preserves the full HTML snapshot.

---

Feel free to commit changes and deploy the static site to any simple host (GitHub Pages, Netlify, etc.).
