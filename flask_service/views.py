# -*- coding: utf-8 -*-
from flask_service import app


@app.route('/')
def index():
    return 'Hello World!'
