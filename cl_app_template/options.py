import argparse
import os

def get_parser():
    parser = argparse.ArgumentParser(
        prog='cl-app-template',
        description='Sample command line application.')

    parser.add_argument(
        'ARG1',
        help='sample argument 1')

    parser.add_argument(
        '--do',
        dest='ARG2',
        default=os.getcwd(),
        help='sample argument 2')

    return parser
