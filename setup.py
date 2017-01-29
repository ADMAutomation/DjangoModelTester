#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup
import adm_modeltester

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='adm_modeltester',
    version=adm_modeltester.__version__,
    #packages=find_packages(),
    packages=['adm_modeltester'], 
    include_package_data=True,
    install_requires=[
        'django', 
        'django-autofixture',
    ], 
    license=adm_modeltester.__license__,  # example license
    description='Some django model tests',
    long_description=README,
    url=adm_modeltester.__url__,
    author=adm_modeltester.__author__,
    author_email=adm_modeltester.__author_email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',  # keep updated "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' + adm_modeltester.__license__,  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
