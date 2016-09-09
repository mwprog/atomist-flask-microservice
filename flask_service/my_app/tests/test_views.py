# -*- coding: utf-8 -*-
from flask import url_for


def test_my_app_index(client):
    res = client.get(url_for('my_app_app.index'))
    assert res.data == b'Hello World!'
