# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)

import flask_service.views

__version__ = '0.0.1'
