from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_restful import Api
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
api = Api()
ma = Marshmallow()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    ma.init_app(app)

    from main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
