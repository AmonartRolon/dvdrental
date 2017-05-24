from flask import render_template
from flask import url_for
from app.films.models import Film
from app import db
from . import films
from flask_login import login_required

@films.route('/browse')
@login_required
def browse():
    films = Film.query.all()
    return render_template('films/browse.html', films = films)

@films.route('/<int:id>')
@login_required
def films(id):
    film = Film.query.get(id)
    return render_template('films/film.html', film = film)
