from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def crate_app():
    app = Flask(__name__)

    app.config['SECERET_KEY'] = "your-secret-key"
    app.config['SQL_DATABAS_URI'] = "sqllite:///shop.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import products_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)


    return app