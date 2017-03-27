from flask import Blueprint
from flask import render_template
from app import app

mod = Blueprint('app', __name__, url_prefix = '/')

@mod.route('/')
def index():
    return render_template('/main/index.html') 
