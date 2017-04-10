from flask import Blueprint

films = Blueprint('films', __name__)

from . import views
