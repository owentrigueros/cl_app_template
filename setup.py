#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cl_app_template',
    version='1.0',
    description='A command-line application template',
    author='Your Name',
    author_email='your_email@your_email_service.com',
    keywords='template command line app application argparse options',
    packages=find_packages(),
    scripts=['bin/cl_app_template'],
    install_requires=[
        '',
    ]
)
