from flask import render_template
from flask import Blueprint
from flask import url_for
from app.languages.models import Language
from app import db
from . import languages

@languages.route('/browse')
def browse():
    languages = Language.query.all()
    return render_template('languages/browse.html', languages = languages)

@languages.route('/<id>')
def languages(id):
    language = Language.query.get(id)
    return render_template('languages/language.html', language = language)
