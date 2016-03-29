#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
from distutils.core import setup
from setuptest import test


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requirements():
    requirements = codecs.open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()
    return list(map(lambda x: x.strip(), requirements))


def get_packages(package):
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    filepaths = ['../README.md', '../requirements.txt', '../requirements-dev.txt']
    return {package: filepaths}

setup(
    name='test_kudago_import',
    version='1.0.1',
    packages=get_packages('test_kudago_import'),
    package_data=get_package_data('test_kudago_import'),
    long_description=read("README.md"),
    install_requires=read_requirements(),
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
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
