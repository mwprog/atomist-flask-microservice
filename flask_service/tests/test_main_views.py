# -*- coding: utf-8 -*-
from flask import url_for


def test_swagger_endpoint(client):
    res = client.get(url_for('main_app.api'))
    assert isinstance(res.data, dict)
