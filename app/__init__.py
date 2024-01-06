from flask import Flask
from .views.main import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    app.register_blueprint(main_blueprint)

    return app
