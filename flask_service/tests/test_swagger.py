# -*- coding: utf-8 -*-
from flask_service.swagger import spec
from flask_service import __version__


def test_document_meta():
    api = spec.to_dict()
    assert api['info']['title'] == 'flask_service'
    assert api['info']['version'] == __version__
    assert api['info']['description'] == 'My application'


def test_document_health_endpoint():
    api = spec.to_dict()
    assert '/health' in api['paths']
    assert 'get' in api['paths']['/health']
    assert '200' in api['paths']['/health']['get']['responses']
    assert 'string' in api['paths']['/health']['get']['responses']['200']['schema']
    assert '503' in api['paths']['/health']['get']['responses']
    assert 'string' in api['paths']['/health']['get']['responses']['503']['schema']


def test_document_status_endpoint():
    api = spec.to_dict()
    assert '/status' in api['paths']
    assert 'get' in api['paths']['/status']
    assert '200' in api['paths']['/status']['get']['responses']
    assert 'string' in api['paths']['/status']['get']['responses']['200']['schema']


def test_document_my_app_endpoint():
    api = spec.to_dict()
    assert '/' in api['paths']
    assert 'get' in api['paths']['/']
    assert '200' in api['paths']['/']['get']['responses']
    assert 'string' in api['paths']['/']['get']['responses']['200']['schema']