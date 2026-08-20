# Anime Recs

A Flask web app for anime recommendations. Anime listings (posters, titles, synopses, genres, reviews) are fetched live from the [AniList GraphQL API](https://docs.anilist.co/) and cached locally in `anilist_cache.json` for 24 hours, so an internet connection is needed on first run (or whenever the cache expires).

## Requirements

- Python 3.9+
- Flask
- requests

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

The app runs in debug mode at `http://127.0.0.1:5000/`.

## Project Structure

```
main.py            # Flask app entry point
templates/          # HTML templates
static/              # Static assets (CSS, JS, images)
docs/                # Project documentation
```
