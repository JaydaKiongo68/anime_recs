ANIME_LIST = [
    {
        "id": "frieren",
        "title": "Frieren: Beyond Journey's End",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "An elf mage who outlives her human companions sets out on a slow, "
            "reflective journey to understand the people she traveled with and "
            "the meaning of the time she spent with them."
        ),
        "genres": ["Fantasy", "Drama", "Adventure"],
        "featured": True,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "concept-art", "path": "images/concept-art/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "quietmage", "rating": 5, "text": "The most patient, gentle storytelling I've seen in the genre. Every episode lingers exactly as long as it should."},
            {"reviewer_name": "himmel_fan", "rating": 5, "text": "Made me cry over a flashback about a flower. Incredible restraint."},
            {"reviewer_name": "actionwatcher22", "rating": 3, "text": "Beautifully made, but the pacing is too slow if you're here for fights."},
        ],
    },
    {
        "id": "jujutsu-kaisen",
        "title": "Jujutsu Kaisen",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "A high schooler swallows a cursed talisman to save his friends and is "
            "pulled into a hidden world of sorcerers who battle monsters born from "
            "human negativity."
        ),
        "genres": ["Action", "Supernatural", "Shounen"],
        "featured": True,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "concept-art", "path": "images/concept-art/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "cursed_energy", "rating": 5, "text": "Fight choreography is on another level. The animation during domain expansions is worth it alone."},
            {"reviewer_name": "sukuna_stan", "rating": 4, "text": "Great cast, occasionally rushes arcs that deserved more room to breathe."},
        ],
    },
    {
        "id": "spy-x-family",
        "title": "Spy x Family",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "A spy, an assassin, and a telepath form a fake family to keep the "
            "peace between two nations, each hiding their true identity from "
            "the others."
        ),
        "genres": ["Comedy", "Slice of Life", "Action"],
        "featured": True,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "anya_waku", "rating": 5, "text": "Wholesome and funny in equal measure. Anya carries every episode she's in."},
            {"reviewer_name": "peanuts4life", "rating": 4, "text": "Consistently charming, though the mission-of-the-week plots can feel low stakes."},
        ],
    },
    {
        "id": "fullmetal-alchemist-brotherhood",
        "title": "Fullmetal Alchemist: Brotherhood",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "Two brothers who lost their bodies attempting a forbidden alchemical "
            "ritual search for a legendary stone that could restore what they "
            "sacrificed, uncovering a conspiracy that reaches their nation's throne."
        ),
        "genres": ["Action", "Adventure", "Drama", "Fantasy"],
        "featured": False,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "concept-art", "path": "images/concept-art/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "equivalent_trade", "rating": 5, "text": "About as close to a perfect shounen arc as the medium has produced. Every character gets a real ending."},
            {"reviewer_name": "roy_mustang_fan", "rating": 5, "text": "Rewatched it three times and it still holds up completely."},
        ],
    },
    {
        "id": "my-hero-academia",
        "title": "My Hero Academia",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "In a world where most people are born with superpowers, a boy with "
            "none enrolls in a school for heroes after inheriting the abilities "
            "of the greatest hero alive."
        ),
        "genres": ["Action", "Shounen", "Superhero"],
        "featured": False,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "plus_ultra", "rating": 4, "text": "Great character work early on, though later seasons juggle too large a cast at once."},
            {"reviewer_name": "deku_diary", "rating": 3, "text": "Solid but the formula has gotten a bit predictable by this point."},
        ],
    },
    {
        "id": "demon-slayer",
        "title": "Demon Slayer",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "After his family is slaughtered and his sister turned into a demon, "
            "a young charcoal seller trains as a demon slayer to find a cure and "
            "avenge the ones he lost."
        ),
        "genres": ["Action", "Supernatural", "Historical"],
        "featured": False,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
            {"type": "concept-art", "path": "images/concept-art/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "nezuko_box", "rating": 5, "text": "The animation during the big fights is genuinely jaw-dropping, especially on a big screen."},
            {"reviewer_name": "tanjiro_nose", "rating": 4, "text": "Gorgeous, if you can tolerate a fairly by-the-numbers shounen story underneath it."},
        ],
    },
    {
        "id": "attack-on-titan",
        "title": "Attack on Titan",
        "cover": "images/posters/placeholder.svg",
        "synopsis": (
            "Humanity's last remnants live behind massive walls to keep out "
            "man-eating giants, until a breach forces a young soldier to confront "
            "the true origin of the threat he's sworn to destroy."
        ),
        "genres": ["Action", "Drama", "Mystery"],
        "featured": False,
        "gallery": [
            {"type": "screenshot", "path": "images/screenshots/placeholder.svg"},
        ],
        "reviews": [
            {"reviewer_name": "wall_maria", "rating": 5, "text": "Starts as a monster story and ends as one of the most ambitious political dramas in anime."},
            {"reviewer_name": "survey_corps99", "rating": 4, "text": "The back half asks a lot of patience from viewers who came for titan fights, but it pays off."},
        ],
    },
]


def get_anime_by_id(anime_id):
    return next((a for a in ANIME_LIST if a["id"] == anime_id), None)


def get_average_rating(anime):
    reviews = anime.get("reviews", [])
    if not reviews:
        return 0.0
    return sum(r["rating"] for r in reviews) / len(reviews)
