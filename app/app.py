# -*- coding: utf-8 -*-

"""The app module, containing the app factory function."""
from flask import Flask
from app import user


def create_app(config=None):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)

