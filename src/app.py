from flask import Flask

from src.endpoints.cut_string import cut_string

app = Flask(__name__)

app.register_blueprint(cut_string)