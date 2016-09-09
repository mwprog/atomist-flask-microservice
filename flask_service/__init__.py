# -*- coding: utf-8 -*-
from flask import Flask

__version__ = '0.0.1'
__all__ = ['create_app']


def create_app() -> 'flask.app.Flask':
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from flask_service.my_app.views import the_app_app
    app.register_blueprint(the_app_app)

    return app
