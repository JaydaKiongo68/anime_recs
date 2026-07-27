# Design System — Anime Review Site

Dark-themed site. Colors and type follow a 60/30/10 split, extracted from `docs/fonts.png`. Font pairing is **Option 2 — "Comic-Book Burst"**: **Bangers** + **Poppins**. This doc is the source of truth for `static/css/styles.css`.

## Color System (60/30/10)

| Role | Hex | Usage % | Where it's used |
|---|---|---|---|
| **Black (Background / Dominant)** | `#252525` | 60% | Page background, cards, nav bar, footer, section surfaces |
| **White (Foreground)** | `#FFFDF7` | 30% | Body text, headings, borders/dividers, icon strokes |
| **Red (Accent)** | `#D52C16` | 10% | CTAs/buttons, links + hover states, star ratings, tag/badge chips, active nav underline |

> **Note on the source image:** `docs/fonts.png` labels its swatches `GROUND #FFFDF7` (60%) and `TEXT #252525` (30%) for a *light* layout. This site is dark-themed, so the roles are deliberately flipped: `#252525` becomes the dominant 60% background color and `#FFFDF7` becomes the 30% foreground/text color. The hex values are unchanged — only which one is "dominant" vs. "foreground" is swapped. `#D52C16` stays the 10% accent in both readings.

### CSS custom properties

```css
:root {
  --color-black: #252525;   /* 60% — background */
  --color-white: #FFFDF7;   /* 30% — foreground/text */
  --color-red:   #D52C16;   /* 10% — accent */
}
```

## Typography — Bangers + Poppins

Chosen pairing: **02 · COMIC-BOOK BURST** from `docs/fonts.png`.

| Font | Role | Notes |
|---|---|---|
| **Bangers** | Display / headings | Comic-lettering display face. High energy, built-in uppercase feel. Use for H1/H2, hero titles, anime titles on cards, section banners. Do not use for body copy or long text — it's a display face and hurts readability at small sizes. |
| **Poppins** | Body / UI | Geometric sans-serif. Use for paragraphs, nav links, buttons, form labels, review text, metadata. |

Both are free on Google Fonts. Per the existing sitemap note, self-host the `.woff2` files for these two only (no need to embed the full 12-font specimen set on the live site).

### Suggested type scale

| Element | Font | Size | Weight | Color |
|---|---|---|---|---|
| H1 (hero/page title) | Bangers | 48–64px | Regular | `--color-white` |
| H2 (section heading) | Bangers | 32–40px | Regular | `--color-white` |
| H3 (card/anime title) | Bangers | 22–28px | Regular | `--color-white` |
| Body text | Poppins | 16px | Regular (400) | `--color-white` |
| Nav / buttons | Poppins | 14–16px | Medium (500) | `--color-white`, `--color-red` on hover/active |
| Small / metadata | Poppins | 12–13px | Regular (400) | `--color-white` at reduced opacity |

```css
h1, h2, h3, .display {
  font-family: "Bangers", cursive;
}

body, p, a, button, input, label {
  font-family: "Poppins", sans-serif;
}
```

## Usage Guidelines

- **Don't invert the ratio.** No large flat-red backgrounds and no white-dominant sections — red stays an accent, not a surface color.
- **Red is reserved for interactive/attention elements**: buttons, links, star ratings, tags, active states. Don't use it for large decorative blocks or body text.
- **Contrast:** `#FFFDF7` text on `#252525` background is near-white on near-black — passes WCAG AA/AAA comfortably for body text.
- **Bangers is headline-only.** Never set paragraph or review body text in Bangers; pair every Bangers heading with Poppins body copy underneath.

## Reference

- Derived from `docs/fonts.png`, pairing **02 (Bangers + Poppins)**.
- Applies to `static/css/styles.css` and all templates listed in `docs/sitemap_official.md` (`base.html`, `index.html`, `browse.html`, `anime.html`).
