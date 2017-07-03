import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()
admin = Admin()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from app.auth.models import User, Role
    from app.films.models import Film, FilmCategory
    from app.categories.models import Category
    from app.languages.models import Language

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(Film, db.session))
    admin.add_view(ModelView(FilmCategory, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Language, db.session))

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from app.languages import languages as languages_blueprint
    app.register_blueprint(languages_blueprint, url_prefix='/languages')
    
    from app.films import films as films_blueprint
    app.register_blueprint(films_blueprint, url_prefix='/films')

    return app
