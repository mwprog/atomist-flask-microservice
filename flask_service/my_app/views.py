# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['the_app_app']

the_app_app = Blueprint('the_app_app', __name__)


@the_app_app.route('/')
def index():
    return "Hello World!"
