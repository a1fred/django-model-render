#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='model_render',
    version='0.1',
    description='Django models extension that allows define default model templates',
    author='a1fred',
    author_email='demalf@gmail.com',
    license='MIT',
    packages=['model_render'],
    zip_safe=False,
    install_requires = [
        'django>=1.4',
    ],
    )
