from flask import Flask
from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()

def crate_app():
    app = Flask(__name__)

    app.config['SECERET_KEY'] = "your-secret-key"

    return app