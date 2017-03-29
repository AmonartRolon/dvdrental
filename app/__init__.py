from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import url_for
from flask_moment import Moment

app = Flask(__name__)
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
