#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
from setuptools import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_packages(package):
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    filepaths = ['../README.md', '../requirements.txt', '../requirements-dev.txt']
    return {package: filepaths}

setup(
    name='test_kudago_import',
    version='1.0.2',
    packages=get_packages('test_kudago_import'),
    package_data=get_package_data('test_kudago_import'),
    long_description=read("README.md"),
    install_requires=[
        'untangle==1.1.0',
    ],
    url='https://github.com/vir-mir/test_kudago',
    license='MIT',
    author='vir-mir',
    keywords='django test kudago',
    author_email='virmir49@gmail.com',
    description='django test kudago, import: xml, json feed',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4.3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Enable django-setuptest
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        # Required by django-setuptools on Python 2.6
        'argparse'
    ),
)
