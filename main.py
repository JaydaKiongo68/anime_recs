from itertools import groupby

from flask import Flask, render_template, abort

from data import ANIME_LIST, get_anime_by_id, get_average_rating

app = Flask(__name__)


@app.route('/')
def home():
    featured = [a for a in ANIME_LIST if a.get('featured')] or ANIME_LIST[:4]
    featured = [{'anime': a, 'avg_rating': get_average_rating(a)} for a in featured]
    return render_template('index.html', featured=featured)


@app.route('/browse')
def browse():
    entries = [{'anime': a, 'avg_rating': get_average_rating(a)} for a in ANIME_LIST]
    entries.sort(key=lambda e: e['anime']['title'].upper())
    top_rated = sorted(entries, key=lambda e: e['avg_rating'], reverse=True)[:5]

    letter_groups = [
        {'letter': letter, 'entries': list(group)}
        for letter, group in groupby(entries, key=lambda e: e['anime']['title'][0].upper())
    ]

    return render_template(
        'browse.html',
        letter_groups=letter_groups,
        top_rated=top_rated,
    )


@app.route('/anime/<anime_id>')
def anime_detail(anime_id):
    anime = get_anime_by_id(anime_id)
    if anime is None:
        abort(404)
    return render_template('anime.html', anime=anime, avg_rating=get_average_rating(anime))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
