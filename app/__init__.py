from flask import Flask

app = Flask(__name__)

from app.main.views import mod as mainModule
app.register_blueprint(mainModule)
