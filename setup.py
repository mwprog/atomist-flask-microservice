# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from flask_service import __version__


setup(
    name = "flask_service",
    version = __version__,
    description = "Flask based microservice.",
    maintainer = "Atomist",
    packages = ["flask_service"],
    platforms = ["any"]
)
