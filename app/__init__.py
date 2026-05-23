from flask import Flask
from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()

def crate_app():
    app = Flask(__name__)

    app.secret_key = 'my-secret-key'

    return app