import json
import logging
import re
import time
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

ANILIST_URL = "https://graphql.anilist.co"
CACHE_PATH = Path(__file__).parent / "anilist_cache.json"
CACHE_TTL_SECONDS = 24 * 60 * 60  # 24h

# Titles from docs/watchlist.md, used as AniList search seeds. The final
# title shown on the site always comes back from the API response, not
# from this list.
WATCHLIST = [
    # Series
    "Jujutsu Kaisen",
    "My Hero Academia",
    "Assassination Classroom",
    "Dr. Stone",
    "Haikyuu!!",
    "Spy x Family",
    "Fire Force",
    "Solo Leveling",
    "Death Note",
    "Blue Lock",
    "Wind Breaker",
    "One Punch Man",
    "Avatar: The Last Airbender",
    "Naruto",
    "Attack on Titan",
    "Chainsaw Man",
    "Black Clover",
    "Komi Can't Communicate",
    # Movies
    "A Whisker Away",
    "Words Bubble Up Like Soda Pop",
    "Your Name.",
    "Bubble",
    "Ponyo",
    "A Silent Voice",
]

# Pins a watchlist title to a specific AniList numeric ID when AniList's
# fuzzy search picks the wrong match. Fill in after inspecting a live run
# (find the correct ID at https://anilist.co/anime/<id>).
TITLE_ID_OVERRIDES = {
    # Bare "Kimi no Na wa" search matches a same-named Suntory water
    # commercial (id 97962) ahead of the actual film.
    "Your Name.": 21519,
    # Bare search matches "Komi Can't Communicate Part 2" (the sequel
    # season) ahead of the original season.
    "Komi Can't Communicate": 133965,
}

_MEDIA_FIELDS = """
    id
    title { romaji english }
    description(asHtml: false)
    coverImage { extraLarge }
    genres
    reviews(sort: RATING_DESC, perPage: 3) {
      nodes {
        summary
        score
        user { name }
      }
    }
"""


def _build_batch_query(titles):
    # Each alias wraps Media in a Page(media: ...) list lookup rather than
    # calling Media(search: ...) directly. A direct Media(search:) call
    # throws a fatal "Not Found" error when a title has zero matches (e.g.
    # "Avatar: The Last Airbender" isn't in AniList's catalog since it's
    # not Japanese animation), and AniList nulls out the *entire* batched
    # response - including every other alias - when that happens. The
    # Page(media:) list form just returns an empty list instead, so one
    # unmatched title can't take down the whole fetch.
    parts = []
    for i, title in enumerate(titles):
        override_id = TITLE_ID_OVERRIDES.get(title)
        if override_id:
            selector = f"id: {override_id}"
        else:
            safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
            selector = f'search: "{safe_title}"'
        parts.append(
            f"m{i}: Page(perPage: 1) {{ media({selector}, type: ANIME) {{ {_MEDIA_FIELDS} }} }}"
        )
    return "query {\n" + "\n".join(parts) + "\n}"


def _fetch_from_anilist(titles):
    query = _build_batch_query(titles)
    resp = requests.post(ANILIST_URL, json={"query": query}, timeout=15)
    try:
        payload = resp.json()
    except ValueError:
        resp.raise_for_status()
        raise

    # AniList responds with a non-2xx status (e.g. 404) whenever any single
    # aliased field errors out (like a search with zero matches), even
    # though the rest of the batched fields still come back with data - so
    # errors are logged per-field rather than treated as a total failure.
    for err in payload.get("errors") or []:
        logger.warning("AniList query error: %s", err.get("message"))

    return payload.get("data") or {}


def _map_media_to_entry(media):
    title_obj = media.get("title") or {}
    title = title_obj.get("english") or title_obj.get("romaji") or "Unknown Title"

    raw_desc = media.get("description") or ""
    synopsis = re.sub(r"<[^>]+>", "", raw_desc).strip()

    cover = (media.get("coverImage") or {}).get("extraLarge") or ""

    genres = media.get("genres") or []

    reviews = []
    for node in (media.get("reviews") or {}).get("nodes") or []:
        score = node.get("score")
        rating = round((score or 0) / 20, 1)
        reviews.append(
            {
                "reviewer_name": (node.get("user") or {}).get("name") or "Anonymous",
                "rating": rating,
                "text": (node.get("summary") or "").strip(),
            }
        )

    return {
        "id": str(media["id"]),
        "title": title,
        "cover": cover,
        "synopsis": synopsis,
        "genres": genres,
        "reviews": reviews,
    }


def _load_cache():
    if not CACHE_PATH.exists():
        return None
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        logger.warning("Failed to read anilist_cache.json: %s", e)
        return None


def _save_cache(anime_list):
    try:
        CACHE_PATH.write_text(
            json.dumps({"fetched_at": time.time(), "anime_list": anime_list}, indent=2),
            encoding="utf-8",
        )
    except OSError as e:
        logger.warning("Failed to write anilist_cache.json: %s", e)


def _cache_is_fresh(cache):
    if not cache:
        return False
    return (time.time() - cache.get("fetched_at", 0)) < CACHE_TTL_SECONDS


def _build_anime_list():
    cache = _load_cache()
    if _cache_is_fresh(cache):
        return cache["anime_list"]

    try:
        raw = _fetch_from_anilist(WATCHLIST)
    except (requests.RequestException, ValueError) as e:
        logger.warning("AniList fetch failed (%s); falling back to stale cache if available.", e)
        if cache:
            return cache["anime_list"]
        return []

    anime_list = []
    for i, title in enumerate(WATCHLIST):
        results = ((raw.get(f"m{i}") or {}).get("media")) or []
        media = results[0] if results else None
        if media is None:
            logger.warning("No AniList match for watchlist title: %r - skipping.", title)
            continue
        anime_list.append(_map_media_to_entry(media))

    if not anime_list and cache:
        logger.warning("AniList returned no usable entries; falling back to stale cache.")
        return cache["anime_list"]

    _save_cache(anime_list)
    return anime_list


ANIME_LIST = _build_anime_list()


def get_anime_by_id(anime_id):
    return next((a for a in ANIME_LIST if a["id"] == anime_id), None)


def get_average_rating(anime):
    reviews = anime.get("reviews", [])
    if not reviews:
        return 0.0
    return sum(r["rating"] for r in reviews) / len(reviews)
