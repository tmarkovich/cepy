# Copyright 2017 Gamalon, Inc.
#
# This file is part of cepy.
#
# cepy is distributed under the Apache 2.0 license.
import codecs
import os
import re
from setuptools import find_packages
from setuptools import setup

#: A regular expression capturing the version number from Python code.

setup(
    name='cepy',
    version='0.0.1',
    description='CFFI bindings for the Cephes special function library',
    author='Gamalon, Inc.',
    author_email='opensource@gamalon.com',
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["cepy/build_cephes.py:ffibuilder"],
    test_suite='nose.collector',
    tests_require=['nose', 'goftests>=0.2.3'],
    # TODO May want to exclude tests here.
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
