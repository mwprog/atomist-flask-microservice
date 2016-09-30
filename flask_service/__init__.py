# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify

from flask_service.swagger import spec

__version__ = '0.0.1'
__all__ = ['create_app']


def create_app() -> Flask:
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from flask_service.views import main_app
    app.register_blueprint(main_app)

    from flask_service.my_app.views import the_app_app
    app.register_blueprint(the_app_app)

    return app

