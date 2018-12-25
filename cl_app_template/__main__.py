#!/usr/bin/env python

import sys

if __package__ is None:
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import cl_app_template

if __name__ == '__main__':
    cl_app_template.main()
