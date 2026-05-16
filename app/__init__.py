from flask import Flask

def crate_app():
    app = Flask(__name__)

    app.secret_key = 'my-secret-key'

    return app