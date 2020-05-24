# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="flyplanner",
    version="0.0.1",
    description="fly planner for happy.developper.fr",
    long_description=readme,
    author="COTTET Julien",
    author_email="happy.developper.fr@gmail.com",
    url="https://github.com/happy-developer-fr/fly-planner",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)