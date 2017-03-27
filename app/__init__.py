from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from app.main.views import mod as mainModule
app.register_blueprint(mainModule)
