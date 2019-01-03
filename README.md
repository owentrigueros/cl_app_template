# A command-line application template written for Python 3
This app can do whatever you want, just write it down.

## Some useful commands
To set up a virtual enviromnet (inside a folder called 'venv'):

    python -m venv venv/

To activate the virtual environment:

    source venv/bin/activate

To deactivate the virtual environment:

    deactivate

Edit requirements.txt to specify your environment's required packages.

Update setup.py with your application information, don't forget to add a list of the minimal packages your app needs to run to 'install_requires' list.

To install requirements:

    pip install -r requirements.txt

To run the application without installing it with pip (for testing or whatever):

    python cl_app_template/__main__.py

To build your package:

    make build

To install your package as non-root user (keep in mind that you may be inside a virtual environment when executing this command, if you know what I mean):

    make install

To remove shit created when building the package:

    make clean

Edit Makefile to automatize whatever you want.
