# Anime Review Site — Sitemap

Backend: Flask. Data still lives in a single Python file (no database yet) — Flask routes read from it and render Jinja2 templates.

## Routes / Pages

### 1. Home — `GET /`
- Site intro/header
- Preview gallery of a few featured anime (pulled from `data.py`)
- Links to Browse page
- Renders `templates/index.html`

### 2. Browse — `GET /browse`
- Full gallery grid of all anime
- Each card shows: cover image, title, average star rating
- Click into any card → Anime Detail page
- Renders `templates/browse.html`

### 3. Anime Detail — `GET /anime/<anime_id>`
- Flask reads `anime_id` from the URL and looks it up in `data.py`
- Sections:
  - Title + cover image
  - Synopsis
  - Genre tags
  - Image gallery (screenshots, concept art)
  - Reviews list (reviewer name, star rating, review text)
- Renders `templates/anime.html`

## File Structure

```
anime-review-site/
├── app.py                  (Flask app + routes)
├── data.py                 (all anime + review data, as Python list/dicts)
├── templates/
│   ├── base.html           (shared layout: nav, footer, block content)
│   ├── index.html          (extends base, Home)
│   ├── browse.html         (extends base, Browse)
│   └── anime.html          (extends base, Anime Detail)
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js       (any client-side interactivity, e.g. gallery tabs)
│   └── images/
│       ├── posters/
│       ├── screenshots/
│       └── concept-art/
```

## Content Fields per Anime (in `data.py`)
- Title
- Cover image
- Synopsis
- Genre(s)
- Gallery images (screenshots, concept art)
- Reviews (reviewer name, star rating, review text)

## Notes
- Average star rating is computed in the Flask route (or a helper function) by looping over the anime's `reviews` list — no need to store it separately.
- `base.html` holds the shared layout (nav bar, footer) so `index.html`, `browse.html`, and `anime.html` just extend it and fill in `{% block content %}`.
- Flask's `url_for('static', filename=...)` should be used for all CSS/JS/image references instead of hardcoded paths.
