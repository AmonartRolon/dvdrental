from flask import render_template
from flask import url_for
from app.films.models import Film
from app import db
from . import films
from flask_login import login_required
from .forms import CategorySelectionForm

@films.route('/browse', methods = ['GET', 'POST'])
@login_required
def browse():
    category_select = CategorySelectionForm()
    if category_select.validate_on_submit():
        films = Film.query.filter_by(category_id = category_select.data)
    else:
        films = Film.query.all()
    return render_template('films/browse.html', films = films,
            category_select = category_select)

@films.route('/<int:id>')
@login_required
def films(id):
    film = Film.query.get(id)
    return render_template('films/film.html', film = film)
