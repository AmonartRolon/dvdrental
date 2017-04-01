from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'it will be changed sometime in the future'

app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:postgres@localhost:5432/dvdrental'
app.config['SQLALCHMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


from app.main.views import mod as mainModule
app.register_blueprint(mainModule)
