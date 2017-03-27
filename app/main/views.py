from flask import Blueprint
from app import app

mod = Blueprint('app', __name__, url_prefix = '/')

@mod.route('/')
def index():
    return 'Index'
