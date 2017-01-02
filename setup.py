#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'django>=1.4',
]

setup(
    name='django-model-render',
    version='0.5',
    description='Django models extension that allows define default model templates',
    author='a1fred',
    author_email='demalf@gmail.com',
    license='MIT',
    url='https://github.com/a1fred/django-model-render',
    packages=['model_render'],
    test_suite="runtests",
    platforms=['any'],
    zip_safe=False,
    install_requires=requirements,
    tests_require=requirements,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
